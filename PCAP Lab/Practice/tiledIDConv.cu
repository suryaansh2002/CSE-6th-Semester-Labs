#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>

#define WIDTH 16
#define MASK_WIDTH 5
#define TILE_WIDTH 4
__constant__ M[MASK_WIDTH];
__global__ oneDTiledConv(int *N, int *P)
{
    __shared__ n_shared[TILE_WIDTH + MASK_WIDTH - 1];
    int id = blockIdx.x * blockDim.x + threadIdx.x;
    int n = MASK_WIDTH / 2;
    int halo_left = (blockIdx.x - 1) * blockDim.x + threadIdx.x;
    int halo_right = (blockIdx.x + 1) * blockDim.x + threadIdx.x;

    if (threadIdx.x > blockDim.x - n)
    {
        n_shared[threadIdx.x - (blockDim.x - n)] = halo_left < 0 ? 0 : N[halo_left];
    }
    n_shared[n + threadIdx.x] = N[id];
    if (threadIdx.x < n)
    {
        n_shared[threadIdx.x + blockDim.x + n] = halo_right > WIDTH ? 0 : N[halo_right];
    }
    __syncthreads();
    int val = 0;
    for (int j = 0; j < MASK_WIDTH; j++)
    {
        val += M[j] * n_shared[threadIdx.x + j];
    }
    P[i] = val;
}

int main()
{
}