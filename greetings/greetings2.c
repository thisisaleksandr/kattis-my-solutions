#include <stdio.h>
#include <string.h>

int main(){
    char str[1001];
    scanf("%s", str);
    int len;
    len = (strlen(str)-2)*2;
    printf("h");
    for(int i=0;i<len; i++){
        printf("e");
    }
    printf("y");
}