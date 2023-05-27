#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>

#define WIDTH 4
#define TILE_WIDTH 2
__global__ tileMultiplication(int *M, int *N, int *P)
{
    __shared__ m_shared[TILE_WIDTH][TILE_WIDTH];
    __shared__ n_shared[TILE_WIDTH][TILE_WIDTH];

    int row = blockIdx.y * blockDim.y threadIdx.y;
    int col = blockIdx.x * blockDim.x threadIdx.x;

    int val = 0;
    int phases = WIDTH / TILE_WIDTH;
    for (int i = 0; i < phases; i++)
    {
        m_shared[threadIdx.y][threadIdx.x] = M[row * WIDTH + (i * TILE_WIDTH) + threadIdx.x];
        n_shared[threadIdx.y][threadIdx.x] = M[(threadIdx.y + (i * TILE_WIDTH)) * WIDTH + col];

        __syncthreads();
        for (int j = 0; j < TILE_WIDTH; j++)
        {
            val += m_shared[threadIdx.y][j] * n_shared[j][threadIdx.x];
        }
    }
    P[row * WIDTH + col] = val;
}
int main()
{
}