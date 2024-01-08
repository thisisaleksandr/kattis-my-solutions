#include <stdio.h>

int main() {
    char str[251];
    scanf("%s", str);
    int i=0;
    while(str[i]!='\0'){
        if (str[i] != str[i+1]){
            printf("%c", str[i]);
        }
        i++;
    }
    
    return 0;
}