#include <stdio.h>

int main(){
    int num, counter=0;
    scanf("%d", &num);
    for(int i=0; i<num; i++){
        int x;
        scanf("%d", &x);
        counter += x;
    }
    printf("%d", counter-(num-1));
}