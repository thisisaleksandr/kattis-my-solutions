#include <stdio.h>
#include <string.h>

int main(){
    int i=1;
    char str[101];
    scanf("%s", str);
    printf("%c", str[0]);
    
    while (i<=strlen(str)){
        if (str[i]=='-'){
            printf("%c", str[i+1]);
        }
        i++;
    }
    return 0;
}