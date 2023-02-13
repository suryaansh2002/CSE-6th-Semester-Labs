#include <mpi/mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	int rank, size, N, *numbers, c, i, fact, sum = 0;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if(rank == 0){
		N = size;
		printf("Enter %d values: \n", N);
		numbers = (int *)calloc(N, sizeof(int));
		for(i=0;i<N;i++)
			scanf("%d", &numbers[i]);
	}

	MPI_Scatter(numbers,1,MPI_INT, &c, 1, MPI_INT, 0, MPI_COMM_WORLD);
	fact = 1;
	while(c > 0){
		fact *= c;
		c--;
	}

	MPI_Reduce(&fact, &sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
	
	if(rank == 0){
		printf("The Sum is %d\n", sum);
		free(numbers);
	}
	MPI_Finalize();
	return 0;
}