#include <stdio.h>
#include <cuda.h>
#include <stdlib.h>
#include <math.h>

__host__ __device__ int decToOnesComp(int n)
{
    int binaryNum[32];
    int i = 0;
    while (n > 0)
    {
        binaryNum[i] = n % 2;
        n = n / 2;
        i++;
    }
    int x = 0;
    for (int j = i - 1; j >= 0; j--)
    {
        x = x * 10;
        x += !binaryNum[j];
    }
    return x;
}
__global__ void modfiyMatrixKernel(int *d_mat, int m, int n)
{
    int id = blockIdx.x * blockDim.x + threadIdx.x + 1;
    if (id < m)
    {
        
        for (int k = 1; k < n - 1; k++)
        {
            d_mat[id * n + k] = decToOnesComp(d_mat[id * n + k]);
        }
    }
}
int main()
{

    printf("Enter the no of rows and cols of the matrix: ");
    int m, n;
    scanf("%d %d", &m, &n);
    printf("Enter %d elements of the matrix:\n", m * n);
    int *mat = (int *)malloc(sizeof(int) * n * m);
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &mat[i * n + j]);
        }
    }
    int *d_mat;

    cudaMalloc((void **)&d_mat, sizeof(int) * n * m);

    cudaMemcpy(d_mat, mat, sizeof(int) * n * m, cudaMemcpyHostToDevice);
    modfiyMatrixKernel<<<1, m-2 >>>(d_mat, m, n);
    cudaMemcpy(mat, d_mat, sizeof(int) * n * m, cudaMemcpyDeviceToHost);
    printf("Output matrix is: \n");
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", mat[i * n + j]);
        }
        printf("\n");
    }
}