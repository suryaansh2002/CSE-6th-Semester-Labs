__kernel void stringManupilate(char* inp, char* op){
    int id = get_global_id(0)
    char c1 = inp[2*i];
    char c2 = inp[2*i + 1];

    char c1_out = (char)((int)c1 + 1);
    char c2_out = (char)((int)c2 + 1);
    op[4*i]=c1;
    op[4*i + 1]=c1_out;

    op[4*i + 2]=c2;
    op[4*i + 3]=c2_out;

}

