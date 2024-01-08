#include <stdio.h>

int main(){
    int cases;
    scanf("%d", &cases);
    for(int i=0; i<cases; i++){
        int stop;
        scanf("%d", &stop);
        int count = 0;
        for(int j=0; j<stop; j++){
            count = (count*2)+1;
        }
        printf("%d\n", count);
    }
    return 0;
}