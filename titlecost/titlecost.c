#include <stdio.h>
#include <string.h>

int main(){
    char str[30];
    double num;
    scanf("%s", str);
    scanf("%lf", &num);
    if(strlen(str) > num){
        printf("%.14lf", num);
    }else{
        printf("%d", strlen(str));
    }
    return 0;
}