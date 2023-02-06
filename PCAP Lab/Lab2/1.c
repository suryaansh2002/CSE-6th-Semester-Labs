#include "mpi.h"
#include <stdio.h>

void toggle(char *s)
{
    for (int i = 0; s[i]; i++)
    {
        if (s[i] >= 65 && s[i] <= 90)
            s[i] += 32;
        else if (s[i] >= 97 && s[i] <= 122)
            s[i] -= 32;
    }
}
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
        printf("Enter a word:");
        scanf("%s", buf);
        while (buf[n] != '\0')
        {
            n++;
        }
        dest = 1;
        MPI_Ssend(buf, n, MPI_CHAR, dest, tag, MPI_COMM_WORLD);
        printf("I have sent %s from process 0\n", buf);
        src = 1;
        MPI_Recv(buf, 50, MPI_INT, src, tag, MPI_COMM_WORLD, &status);
        printf("I have received %s in process 0\n", buf);
    }
    else
    {
        src = 0;
        MPI_Recv(buf, 50, MPI_INT, src, tag, MPI_COMM_WORLD, &status);
        printf("I have received %s in process 1\n", buf);
        toggle(buf);
        printf("I have sent %s from process 1\n", buf);
        dest = 0;
        while (buf[n] != '\0')
        {
            n++;
        }
        MPI_Ssend(buf, n, MPI_CHAR, dest, tag, MPI_COMM_WORLD);
    }
    MPI_Finalize();
    return 0;
}