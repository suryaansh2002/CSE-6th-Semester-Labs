#include <cuda.h>
#include <stdlib.h>
#include <stdio.h>

__global__
void FindOccurrencesKernel(char *sentence, char *word, int length){
    int idx = threadIdx.x;
    int  size = length;
    int len = size - idx;
    int sumAll = size * (size+1)/2;
    int sumLess = len * (len+1)/2;
    int start = sumAll - sumLess;
    for (int i=0; i<len;i++){
        sentence[i+start]=word[i];
    }
}

int main(){
    printf("Enter length of word: ");
    int n;
    scanf("%d", &n);
    char *word = (char *)calloc(n, sizeof(char));
    printf("Enter the word: ");
    scanf("%s", word);
    char *final = (char *)calloc(n*(n+1)/2, sizeof(char));
    char *d_final, *d_word;
    cudaMalloc((void **)&d_final, sizeof(char) * n * (n+1)/2);
    cudaMalloc((void **)&d_word, sizeof(char) * n);
    cudaMemcpy(d_final, final, sizeof(char) * (n+1) * n/2, cudaMemcpyHostToDevice);
    cudaMemcpy(d_word, word, sizeof(char) * n, cudaMemcpyHostToDevice);
    FindOccurrencesKernel<<<1, n>>>(d_final, d_word, n);
    cudaMemcpy(final, d_final, sizeof(char) * (n+1) * n/2, cudaMemcpyDeviceToHost);
    printf("Output word is: %s\n", final);
    return 0;
}