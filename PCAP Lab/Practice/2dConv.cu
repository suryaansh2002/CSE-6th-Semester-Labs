#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>

__global__ void twoDimConvKernel(int *d_mask, int *d_arr, int *d_arr_output, int mask_width, int mask_height, int arr_width, int arr_height)
{
    int col = threadIdx.x + blockIdx.x * blockDim.x;
    int row = threadIdx.y + blockIdx.y * blockDim.y;

    int startCol = col - (mask_width - 1) / 2;
    int startRow = row - (mask_height - 1) / 2;
    int sum = 0;
    for (int i = 0; i < mask_width; i++)
    {
        for (int j = 0; j < mask_height; j++)
        {

            if (startCol + i >= 0 && startCol + i < arr_width && startRow + j >= 0 && startRow + j < arr_height)
            {
                sum += d_arr[(startRow + j) * arr_width + (startCol + i)] * d_mask[j * mask_width + i];
            }
        }
    }

    d_arr_output[row * arr_width + col] = sum;
}

int main()
{
    int mask_width = 5;
    int mask_height = 7;
    int mask[mask_height][mask_width];

    // Populating mask matrix with elements from 1 to 35
    for (int i = 0; i < mask_height; i++)
    {
        for (int j = 0; j < mask_width; j++)
        {
            mask[i][j] = i * mask_width + j + 1;
        }
    }

    int arr_height = 10;
    int arr_width = 8;

    int *arr = (int *)malloc(sizeof(int) * arr_height * arr_width);
    int *arr_output = (int *)malloc(sizeof(int) * arr_height * arr_width);

    // Populating input array from 1 to 80
    for (int i = 0; i < arr_height * arr_width; i++)
    {
        arr[i] = i + 1;
    }

    dim3 dimBlock(arr_width, arr_height, 1);
    dim3 dimGrid(1, 1, 1);
    int *d_mask, *d_arr, *d_arr_output;
    cudaMalloc((void **)&d_mask, sizeof(int) * mask_height * mask_width);
    cudaMalloc((void **)&d_arr, sizeof(int) * arr_height * arr_width);
    cudaMalloc((void **)&d_arr_output, sizeof(int) * arr_width * arr_height);

    cudaMemcpy(d_mask, mask, sizeof(int) * mask_width * mask_height, cudaMemcpyHostToDevice);
    cudaMemcpy(d_arr, arr, sizeof(int) * arr_width * arr_height, cudaMemcpyHostToDevice);

    twoDimConvKernel<<<dimGrid, dimBlock>>>(d_mask, d_arr, d_arr_output, mask_width, mask_height, arr_width, arr_height);
    cudaMemcpy(arr_output, d_arr_output, sizeof(int) * arr_height * arr_width, cudaMemcpyDeviceToHost);

    printf("Matrix after Convolution:\n");

    for (int i = 0; i < arr_height; i++)
    {
        for (int j = 0; j < arr_width; j++)
        {
            printf("%d ", arr_output[i * arr_width + j]);
        }
        printf("\n");
    }

    free(arr);
    free(arr_output);
    cudaFree(d_mask);
    cudaFree(d_arr);
    cudaFree(d_arr_output);

    return 0;
}
