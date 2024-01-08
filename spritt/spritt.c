#include <stdio.h>

int main(){
    
    int num1, num2, c=0;
    scanf("%d %d", &num1, &num2);
    for(int i=0; i<num1; i++){
        int num3;
        scanf("%d", &num3);
        c+= num3;
    }
    if (c<=num2){
        printf("Jebb");
    }else{
        printf("Neibb");
    }
    
    return 0;
}