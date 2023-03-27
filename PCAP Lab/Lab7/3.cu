#include <cuda.h>
#include <stdlib.h>
#include <stdio.h>

__global__
void vecAddKernel(float *a, float*b, float *c,int n, int m){
	int i = threadIdx.x + blockIdx.x * blockDim.x;
    int sum=0;
    int mid= (m-1)/2;
    for(int j=0; j<m; j++){
        if((i-mid+j)>=0 && (i-mid+j)<n){
            sum= sum + (a[i-mid+j])*(b[j]);
        }
    }
	c[i] = sum;
}

void vecAdd(float *a,float *c, float *b,int n, int m){
	int size = n * sizeof(float);
	float *d_a,*d_b,*d_c;
	cudaMalloc((void**) &d_a,size);
	cudaMalloc((void**) &d_b,size);
	cudaMalloc((void**) &d_c,size);

	cudaMemcpy(d_a,a,size,cudaMemcpyHostToDevice);
	cudaMemcpy(d_b,b,m * sizeof(float),cudaMemcpyHostToDevice);

	printf("a:");
	for(int i = 0;i<n;i++){
		printf("%.2f,",a[i]);
	}
	printf("\n");
	printf("\n");
	vecAddKernel<<<n,1>>> (d_a,d_b, d_c,n, m);
	cudaMemcpy(c,d_c,size,cudaMemcpyDeviceToHost);
	printf("c:");
	for(int i = 0;i<n;i++){
		printf("%.2f,",c[i]);
	}

	printf("\n");
	printf("\n");
	cudaFree(d_a);
	cudaFree(d_c);
}

int main(){
    int n=8,m=5;
	float ha[8]={1,2,3,4,5,6,7,8};
    float hb[8];
    float mask[5]={1,2,3,4,5};
	vecAdd(ha,hb,mask,n, m);
	return 0;
}