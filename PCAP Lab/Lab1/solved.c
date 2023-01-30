#include<stdio.h>
#include "mpi.h"

int main(int argc, char* argv[]){
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if(rank==0){
    printf("This is 0th process\n");

    }
    else if(rank==2){
        printf("Hello world\n");
    }
    else{

    printf("My rank is %d in total %d processes\n", rank,size);
    }
    MPI_Finalize();
    return 0;

}