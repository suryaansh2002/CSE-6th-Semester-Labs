#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>

__global__ void oneDimConvKernel(int *d_mask, int *d_arr, int *d_arr_output, int mask_width, int arr_size) {
    int index = threadIdx.x + blockIdx.x * blockDim.x;
    int start = index - (mask_width - 1) / 2;
    int sum = 0;
    for (int j = 0; j < mask_width; j++) {
        if (start + j >= 0 && start + j < arr_size) {
            sum += d_arr[start + j] * d_mask[j];
        }
    }
    d_arr_output[index] = sum;
}

int main() {
    int mask[5] = {1, 2, 3, 2, 1};
    int mask_width = 5;
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
    int *d_mask, *d_arr, *d_arr_output;

    cudaMalloc((void **) &d_mask, sizeof(int) * mask_width);
    cudaMalloc((void **) &d_arr, sizeof(int) * arr_size);
    cudaMalloc((void **) &d_arr_output, sizeof(int) * arr_size);

    cudaMemcpy(d_mask, mask, sizeof(int) * mask_width, cudaMemcpyHostToDevice);
    cudaMemcpy(d_arr, arr, sizeof(int) * arr_size, cudaMemcpyHostToDevice);

    oneDimConvKernel<<<dimGrid, dimBlock>>>(d_mask, d_arr, d_arr_output, mask_width, arr_size);

    cudaMemcpy(arr_output, d_arr_output, sizeof(int) * arr_size, cudaMemcpyDeviceToHost);

    printf("Array after Convolution:\n");
    for (int i = 0; i < arr_size; i++) {
        printf("%d ", arr_output[i]);
    }
    printf("\n");

    cudaFree(d_mask);
    cudaFree(d_arr);
    cudaFree(d_arr_output);

    free(arr);
    free(arr_output);

    return 0;
}
