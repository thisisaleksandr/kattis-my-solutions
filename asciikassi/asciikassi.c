#include <stdio.h>

int main(){
    
    int num;
    scanf("%d", &num);
    for(int i=0; i<num+2; i++){
        for(int j=0; j<num+2; j++){
            if(i==0 && j==0 || i==0 && j==num+1 || i==num+1 && j==0 || i==num+1 && j==num+1){
                printf("+");
            }else if(i==0 || i==num+1){
                printf("-");
            }else if (j==0 || j==num+1){
                printf("|");
            }else{
                printf(" ");
            }
        }
        printf("\n");
    }
    
    return 0;
}