#include <stdio.h>

int main(){
    int num, num2, counter=0;
    scanf("%d", &num);
    scanf("%d", &num2);
    for(int i=0; i<num2; i++){
        int num3;
        scanf("%d", &num3);
        counter = counter + num - num3;
    }
    printf("%d", counter+num);
}