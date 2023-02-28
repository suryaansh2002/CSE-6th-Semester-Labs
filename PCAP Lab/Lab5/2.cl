__kernel void vector_add(__global int *A, __global int *C){
    //Get index of the current work item
    
    int i = get_global_id(0);
	int num=A[i];
    C[i] = ~A[i];
}