#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>

#define MASK_WIDTH 5

__constant__ int M[MASK_WIDTH];
__global__ void oneDimConvKernel(int *d_arr, int *d_arr_output,  int arr_size) {
    int index = threadIdx.x + blockIdx.x * blockDim.x;
    int start = index - (MASK_WIDTH - 1) / 2;
    int sum = 0;
    for (int j = 0; j < MASK_WIDTH; j++) {
        if (start + j >= 0 && start + j < arr_size) {
            sum += d_arr[start + j] * M[j];
        }
    }
    d_arr_output[index] = sum;
}

int main() {
    int mask[MASK_WIDTH] = {1, 2, 3, 2, 1};
    int arr_size = 7;
    int *arr = (int *) malloc(sizeof(int) * arr_size);
    int *arr_output = (int *) malloc(sizeof(int) * arr_size);

    printf("Enter %d elements of array:\n", arr_size);
    for (int i = 0; i < arr_size; i++) {
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
    cudaEventRecord(start,0);
    cudaMalloc((void **) &d_arr, sizeof(int) * arr_size);
    cudaMalloc((void **) &d_arr_output, sizeof(int) * arr_size);

    cudaMemcpy(d_arr, arr, sizeof(int) * arr_size, cudaMemcpyHostToDevice);
    cudaMemcpyToSymbol(M,mask, MASK_WIDTH*sizeof(int));
    oneDimConvKernel<<<dimGrid, dimBlock>>>( d_arr, d_arr_output, arr_size);

    cudaMemcpy(arr_output, d_arr_output, sizeof(int) * arr_size, cudaMemcpyDeviceToHost);
    cudaEventRecord(stop,0);
    cudaEventSynchronize(stop);
    float time;
    cudaEventElapsedTime(&time, start, stop);
    printf("Time taken for convolution: %f \n", time);
    printf("Array after Convolution:\n");
    for (int i = 0; i < arr_size; i++) {
        printf("%d ", arr_output[i]);
    }
    printf("\n");

    cudaFree(d_arr);
    cudaFree(d_arr_output);
    free(arr);
    free(arr_output);

    return 0;
}
