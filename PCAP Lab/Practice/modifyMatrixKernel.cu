#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>

__host__ __device__ int isPrime(int x)
{
    for (int i = 2; i * i <= x; i++)
    {
        if (x % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

__global__ void modifyMatrixKernel(int *d_matA, char *d_matB, int *d_n, int *d_m)
{
    int blockId = (blockIdx.z * gridDim.y * gridDim.x) + (blockIdx.y * gridDim.x) + blockIdx.x;
    int threadId = (blockId * blockDim.z * blockDim.y * blockDim.x) + (threadIdx.z * blockDim.y * blockDim.x) + (threadIdx.y * blockDim.x) + threadIdx.x;
    
    if (threadId < *d_n) // Since each thread does for one row
    {
        for (int k = 0; k < *d_m; k++)
        {
            char c;
            int ele = d_matA[threadId * (*d_m) + k];
            if (ele == 0)
            {
                c = 'Z';
            }
            else if (ele == 1)
            {
                c = 'O';
            }
            else if (ele < 0)
            {
                c = 'N';
            }
            else
            {
                if (isPrime(ele) == 1)
                {
                    c = 'P';
                }
                else
                {
                    c = 'C';
                }
            }
            d_matB[threadId * (*d_m) + k] = c;
        }
    }
}

int main()
{
    int n, m;
    printf("Enter number of rows and columns in matrix:");
    scanf("%d", &n);
    scanf("%d", &m);
    printf("Enter %d elements of the matrix:", n * m);
    int *mat = (int *)malloc(sizeof(int) * m * n);
    char *matB = (char *)malloc(sizeof(char) * m * n);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &mat[i * m + j]);
        }
    }
    int *d_mat, *d_n, *d_m;
    char *d_matB;
    cudaMalloc((void **)&d_mat, sizeof(int) * n * m);
    cudaMalloc((void **)&d_matB, sizeof(char) * n * m);
    cudaMalloc((void **)&d_n, sizeof(int));
    cudaMalloc((void **)&d_m, sizeof(int));

    cudaMemcpy(d_mat, mat, sizeof(int) * n * m, cudaMemcpyHostToDevice);
    cudaMemcpy(d_n, &n, sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_m, &m, sizeof(int), cudaMemcpyHostToDevice);
    dim3 dimGrid(3, 4, 3);
    dim3 dimBlock(4, 3, 3);

    modifyMatrixKernel<<<dimGrid, dimBlock>>>(d_mat, d_matB, d_n, d_m);

    cudaMemcpy(matB, d_matB, sizeof(char) * n * m, cudaMemcpyDeviceToHost);

    printf("Output Matrix:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%c", matB[i * m + j]);
        }
    }
}