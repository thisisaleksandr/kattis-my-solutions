#include <stdio.h>

int main(){
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    for(int k=0; k<num1; k++){
        char nothing[1000];
        scanf("%s", nothing);
    }
    printf("%d", num2);
}