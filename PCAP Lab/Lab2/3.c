#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int rank, size, tag = 1, dest, src, n = 0;
    int bs = MPI_BSEND_OVERHEAD + sizeof(int);
    int *buffer = malloc(bs);

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Buffer_attach(buffer, bs);
    MPI_Status status;
    if (rank == 0)
    {
        printf("Enter %d numbers:", size);
        int arr[size];
        for (int i = 0; i < size - 1; i++)
        {
            scanf("%d", &arr[i]);
        }
        printf("In process 0, number is %d, square is %d\n", arr[0], arr[0] * arr[0]);
        for (int i = 1; i < size; i++)
        {
            dest = i;

            MPI_Bsend(&arr[i - 1], 1, MPI_INT, dest, tag, MPI_COMM_WORLD);
        }
    }
    else
    {
        src = 0;
        int a;
        MPI_Recv(&a, 1, MPI_INT, src, tag, MPI_COMM_WORLD, &status);
        if (rank % 2)
        {
            printf("In process %d, number is %d, cube is %d\n", rank, a, a * a * a);
        }
        else
        {
            printf("In process %d, number is %d, square is %d\n", rank, a, a * a);
        }
    MPI_Buffer_detach(&buffer, &bs);
    }
    MPI_Finalize();
    return 0;
}