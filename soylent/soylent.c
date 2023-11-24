#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for(int i = 0; i < num; i++){
        int cal;
        scanf("%d", &cal);
        if(cal%400!=0){
            printf("%d\n", cal/400 + 1);
        }else{
            printf("%d\n", cal/400);
        }
    }
    return 0;
}