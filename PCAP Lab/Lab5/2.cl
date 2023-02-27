__kernel void vector_add(__global char **A, __global char **C){
    //Get index of the current work item
    
    int i = get_global_id(0);
	char *num=A[i];
    int len=0, j=0;
    while(num[j]!='\n'){
        j++;
        len++;
    }
    printf("Nums:\n");
    for(int j=0; j<len; j++){
        printf("%c",num[j]);
    }
    printf("\n");
}