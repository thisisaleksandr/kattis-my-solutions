#include <stdio.h>

int main(){
    int num, counter=0;
    scanf("%d", &num);
    for(int i=0; i<num; i++){
        int exp;
        scanf("%d", &exp);
        if(exp<0){
            counter+=exp;
        }
    }
    printf("%d", counter*-1);
}