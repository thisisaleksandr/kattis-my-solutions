#include <stdio.h>

int main(){
    int num;
    int c1=1, c2=2, c3=4;
    int counter=0;
    scanf("%d", &num);
    if(num==1){
        printf("%d", c1);
    }
    if(num==2){
        printf("%d", c2);
    }
    if(num==3){
        printf("%d", c3);
    }
    if (num>=4){
        for (int i=0; i<num-3; i++){
            counter=c1+c2+c3;
            c1 = c2;
            c2 = c3;
            c3 = counter;
        }
        printf("%d", counter);
    }
    return 0;
}