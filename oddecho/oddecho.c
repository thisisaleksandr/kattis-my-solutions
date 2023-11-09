#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for(int k=0; k<num; k++){
        char str[101];
        scanf("%s", str);
        if (k%2==0){
            printf("%s\n", str);
        }
    }
}