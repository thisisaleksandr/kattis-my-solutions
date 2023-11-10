#include <stdio.h>

int main(){
    int a,b,c;
    int counter=0;
    scanf("%d %d %d", &a, &b, &c);
    for (int i=0; i<a; i++){
        int fr;
        scanf("%d", &fr);
        if (b+c-fr>=14){
            counter++;
        }
    }
    printf("%d", counter);
    
    return 0;
}