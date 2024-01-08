#include <stdio.h>
#include <string.h>

int main(){
    char str[1000];
    fgets(str, 1000, stdin);
    int len = strlen(str);
    if(str[len-2] == '?' && str[len-3] == 'h' && str[len-4] == 'e'){
        printf("Canadian!");
    }else{
        printf("Imposter!");
    }
    return 0;
}