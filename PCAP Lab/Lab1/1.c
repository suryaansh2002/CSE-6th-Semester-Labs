#include<stdio.h>
#include "mpi.h"
#include<math.h>

int main(int argc, char* argv[]){
    int x=2;
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int power =pow(x,rank);
    printf("Rank: %d, X: %d, pow(x,rank)=%d\n", rank,x,power);
    
    MPI_Finalize();
    return 0;

}