#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    if(num%2==1){
        printf("still running");
    }else{
        int counter=0;
        for(int i=0; i<num/2; i++){
            int start, stop;
            scanf("%d", &start);
            scanf("%d", &stop);
            counter+=(stop-start);
        }
        printf("%d", counter); 
    }
    return 0;
}