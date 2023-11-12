#include <stdio.h>
int main(){
    int num, counter=0;
    scanf("%d", &num);
    for(int i=0; i<num; i++){
        int t;
        scanf("%d", &t);
        counter+=t;
    }
    printf("%d", counter/num);
    return 0;
}
