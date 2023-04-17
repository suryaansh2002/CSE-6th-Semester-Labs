#include<stdio.h>
#include<stdlib.h>
int main(){
    int n=8;
    printf("X: %d\n",n);

int binaryNum[32];
  
    // counter for binary array
    int i = 0;
    while (n > 0) {
        // storing remainder in binary array
        binaryNum[i] = n % 2;
        n = n / 2;
        i++;
    }
    int x=0;
    // printing binary array in reverse order
    for (int j = i - 1; j >= 0; j--){
        x=x*10;
        x+=!binaryNum[j];
    }
    printf("%d",x);


}