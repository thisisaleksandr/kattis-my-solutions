#include <stdio.h>

int main(){
    char str[16];
    scanf("%s", str);
    for(int i=1; i<=3; i++){
        printf("%s", str);
        if (i!=3){
            printf(" ");
        }
    }
}