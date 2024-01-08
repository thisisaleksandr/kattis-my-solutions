#include <stdio.h>

int main() {
    int num, counter=0;
    scanf("%d", &num);
    for(int i=0; i<num; i++){
        int num2;
        scanf("%d", &num2);
        if (num2 < 0){
            counter+=1;
        }
    }
    printf("%d", counter);
    return 0;
}