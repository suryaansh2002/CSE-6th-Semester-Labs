#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>

#define MASK_WIDTH 5
#define TILE_SIZE 2

__constant__ int M[MASK_WIDTH];
__global__ void oneDimConvKernel(int *N, int *P, int Mask_Width, int Width)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    __shared__ float N_ds[TILE_SIZE + MASK_WIDTH - 1];
    int n = Mask_Width / 2;
    int halo_index_left = (blockIdx.x - 1) * blockDim.x + threadIdx.x;
    if (threadIdx.x >= blockDim.x - n)
    {
        N_ds[threadIdx.x - (blockDim.x - n)] =
            (halo_index_left < 0) ? 0 : N[halo_index_left];
    }
    N_ds[n + threadIdx.x] = N[blockIdx.x * blockDim.x + threadIdx.x];
    int halo_index_right = (blockIdx.x + 1) * blockDim.x + threadIdx.x;
    if (threadIdx.x < n)
    {
        N_ds[n + blockDim.x + threadIdx.x] =
            (halo_index_right >= Width) ? 0 : N[halo_index_right];
    }
    __syncthreads();
    int Pvalue = 0;
    for (int j = 0; j < Mask_Width; j++)
    {
        Pvalue += N_ds[threadIdx.x + j] * M[j];
    }
    P[i] = Pvalue;
}

int main()
{
    int mask[MASK_WIDTH] = {1, 2, 3, 2, 1};
    int arr_size = 12;
    int *arr = (int *)malloc(sizeof(int) * arr_size);
    int *arr_output = (int *)malloc(sizeof(int) * arr_size);

    printf("Enter %d elements of array:\n", arr_size);
    for (int i = 0; i < arr_size; i++)
    {
        scanf("%d", &arr[i]);
    }
    int threads_per_block = 256;
    int blocks_per_grid = (arr_size + threads_per_block - 1) / threads_per_block;
    dim3 dimBlock(threads_per_block, 1, 1);
    dim3 dimGrid(blocks_per_grid, 1, 1);
    int *d_arr, *d_arr_output;

    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start, 0);
    cudaMalloc((void **)&d_arr, sizeof(int) * arr_size);
    cudaMalloc((void **)&d_arr_output, sizeof(int) * arr_size);

    cudaMemcpy(d_arr, arr, sizeof(int) * arr_size, cudaMemcpyHostToDevice);
    cudaMemcpyToSymbol(M, mask, MASK_WIDTH * sizeof(int));
    oneDimConvKernel<<<4,3>>>(d_arr, d_arr_output, MASK_WIDTH, arr_size);

    cudaMemcpy(arr_output, d_arr_output, sizeof(int) * arr_size, cudaMemcpyDeviceToHost);
    cudaEventRecord(stop, 0);
    cudaEventSynchronize(stop);
    float time;
    cudaEventElapsedTime(&time, start, stop);
    printf("Time taken for convolution: %f \n", time);
    printf("Array after Convolution:\n");
    for (int i = 0; i < arr_size; i++)
    {
        printf("%d ", arr_output[i]);
    }
    printf("\n");

    cudaFree(d_arr);
    cudaFree(d_arr_output);
    free(arr);
    free(arr_output);

    return 0;
}
