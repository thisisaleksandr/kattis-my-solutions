#include <stdio.h>

int main(){
    char str[1001];
    scanf("%s", str);
    int i=0, flag=0;
    while(str[i] != 'a'){
        i++;
    }
    while(str[i] != '\0'){
        printf("%c", str[i]);
        i++;
    }
}