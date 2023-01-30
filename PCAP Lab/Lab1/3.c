#include<stdio.h>
#include "mpi.h"

int main(int argc, char* argv[]){
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int a=6, b=3;

    if(rank==0){
        printf("%d+%d=%d\n",a,b,a+b);
    }
    else if(rank==1){
        printf("%d-%d=%d\n",a,b,a-b);
    }
    else if(rank==2){
        printf("%d*%d=%d\n",a,b,a*b);
    }
    else if(rank==3){
        printf("%d/%d=%d\n",a,b,a/b);
    }
    else{
        printf("Rank:%d\n",rank);
    }
    
    MPI_Finalize();
    return 0;

}