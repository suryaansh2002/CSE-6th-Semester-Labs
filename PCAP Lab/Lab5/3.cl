__kernel void vector_add(__global int *A){
    //Get index of the current work item
    int i = get_global_id(0);
    if(i%2==0){
        int temp=A[i];
        A[i]=A[i+1];
        A[i+1]=temp;
    printf("\n%d, %d\n",A[i], A[i+1]);
    }
}