

int pow(int a, int b){
    int m=1, n=a;
    while(m<b){
        a=a*n;
        m++;
    }
    return a;
}
__kernel void vector_add(__global int *A){
    //Get index of the current work item
    int i = get_global_id(0);
    int n=A[i];
    int p=0;
    int dec=0;
    // array to store octal number
    while(n>0){
        int r=n%10;
        if(r){
        dec+=pow(2,p);
        }
        p++;
        n=n/10;
    }
  C[i]=dec;
}