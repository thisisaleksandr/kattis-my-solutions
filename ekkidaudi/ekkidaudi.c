#include <stdio.h>
#include <string.h>

int main(){
    char str[2101], str2[2101];
    int c1=0, c2=0;
    fgets(str, 2101, stdin);
    fgets(str2, 2101, stdin);
    
    for(int k=0; k<strlen(str); k++){
        if (str[k] != '|') {
            printf("%c", str[k]);
        }else{
            break;
        }
        c1++;
    }
    for(int k=0; k<strlen(str2); k++){
        if (str2[k] != '|') {
            printf("%c", str2[k]);
        }else{
            break;
        }
        c2++;
    }   
    c1++;
    c2++;
    printf(" ");
    while (str[c1] != '\n'){
        printf("%c", str[c1]);
        c1++;
    }
    while (str2[c2] != '\n'){
        printf("%c", str2[c2]);
        c2++;
    }    
   
    return 0;
}