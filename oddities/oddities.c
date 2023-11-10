#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for (int i=0; i<num; i++){
        int num2;
        scanf("%d", &num2);
        if(num2%2==0){
            printf("%d is even", num2);
        }else{
            printf("%d is odd", num2);
        }
        printf("\n");
    }
    return 0;
}