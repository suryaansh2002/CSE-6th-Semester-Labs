 #include<stdio.h>
 #include<cuda.h>
 #include<stdlib.h>
#include<math.h>

__global__ void modfiyMatrixKernel(int*d_mat, int* d_mat_output, int m, int n){
    int id=blockIdx.x*blockDim.x + threadIdx.x;
    if(id<m){
        for(int k=0; k<n; k++){
            d_mat_output[id*n + k]=pow(d_mat[id*n + k], id+1);
        }
    }

}
 int main(){

    printf("Enter the no of rows and cols of the matrix: ");
    int m,n;
    scanf("%d %d", &m, &n);
    printf("Enter %d elements of the matrix:\n", m*n);
    int* mat=(int *)malloc(sizeof(int)*n*m);
    int* mat_output=(int *)malloc(sizeof(int)*n*m);
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            scanf("%d", &mat[i*n + j]);
        }
    }
    int*d_mat, *d_mat_output;

    cudaMalloc((void **) &d_mat, sizeof(int)*n*m);
    cudaMalloc((void **) &d_mat_output, sizeof(int)*n*m);

    cudaMemcpy(d_mat, mat, sizeof(int)*n*m, cudaMemcpyHostToDevice);
    modfiyMatrixKernel<<<1,m>>>(d_mat,d_mat_output, m,n);
    cudaMemcpy(mat_output, d_mat_output, sizeof(int)*n*m, cudaMemcpyDeviceToHost);
    printf("Output matrix is: \n");
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            printf("%d ", mat_output[i*n + j]);
        }
        printf("\n");
    }
 }