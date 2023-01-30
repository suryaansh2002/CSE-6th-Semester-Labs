#include<stdio.h>
#include "mpi.h"

char toggle(char c){
    if(c>=65 && c<=90){
        c=c+32;
    }
    else if(c>=97 && c<=122){
        c=c-32;
    }
return c;
}
int main(int argc, char* argv[]){
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    char h[6]="Hello";
    h[rank]=toggle(h[rank]);
    printf("Rank:%d, %s\n", rank, h);
    MPI_Finalize();
    return 0;

}