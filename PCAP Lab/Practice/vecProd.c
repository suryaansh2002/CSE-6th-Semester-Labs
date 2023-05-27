#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int *a, *b;
    int numA, numB, n;
    if (rank == 0)
    {
        printf("Enter the no. of elements: ");
        scanf("%d", &n);
        a = (int *)malloc(sizeof(int) * n);
        b = (int *)malloc(sizeof(int) * n);
        printf("Enter %d elements of A: ", n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
        }
        printf("Enter %d elements of B: ", n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &b[i]);
        }
    }
    MPI_Scatter(a, 1, MPI_INT, &numA, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Scatter(b, 1, MPI_INT, &numB, 1, MPI_INT, 0, MPI_COMM_WORLD);
    int result = numA * numB;
    int finalResult;
    MPI_Reduce(&result, &finalResult, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    if (rank == 0)
    {
        printf("Vector product is: %d", finalResult);
    }
    MPI_Finalize();
    return 0;
}