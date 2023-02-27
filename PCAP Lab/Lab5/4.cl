

int pow(int a, int b){
    int m=1, n=a;
    while(j<b){
        a=a*n;
        m++;
    }
}
__kernel void vector_add(__global int *A){
    //Get index of the current work item
    int i = get_global_id(0);
    int n=A[i];
    // array to store octal number
    int octalNum[100];
  
    // counter for octal number array
    int x = 0;
    while (n != 0) {
  
        // storing remainder in octal array
        octalNum[x] = n % 8;
        n = n / 8;
        x++;
    }
    int res=0;
    for(int j=x; j>=0; j--){
        res+=pow(2,j);
    }
    
  
}