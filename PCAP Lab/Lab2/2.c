#include "mpi.h"
#include <stdio.h>


int main(int argc, char *argv[])
{
    int rank, size, tag = 1, dest, src, n = 0;
    char buf[50];
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;
    if (rank == 0)
    {
        printf("Enter %d numbers:", size-1);
        int arr[size-1];
        for(int i=0; i<size-1; i++){
            scanf("%d", &arr[i]);
        }
        printf("In process 0, sending %d numbers\n", size-1);
        for(int i=1; i<size; i++){
        dest=i;
        MPI_Send(&arr[i-1], 1, MPI_INT, dest, tag, MPI_COMM_WORLD);

        }
    }
    else
    {
        src = 0;
        int a;
        MPI_Recv(&a, 1, MPI_INT, src, tag, MPI_COMM_WORLD, &status);
        printf("I have received %d in process %d\n", a, rank);

    }
    MPI_Finalize();
    return 0;
}