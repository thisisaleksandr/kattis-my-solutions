#include <stdio.h>
#include <string.h>
int main(){
    char str1[1000], str2[1000];
    scanf("%s", str1);
    scanf("%s", str2);
    if(strlen(str1)>=strlen(str2)){
        printf("go");
    }else{
        printf("no");
    }
}