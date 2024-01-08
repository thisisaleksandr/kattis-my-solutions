#include <stdio.h>
#include <string.h>

int main(){
    char str[100];
    scanf("%s", str);
    int b=0, k=0;
    for(int i=0; i<strlen(str); i++){
        if (str[i]=='b'){
            b++;
        }else if(str[i]=='k'){
            k++;
        }
    }
    if (b>k){
        printf("boba");
    }else if (b<k){
        printf("kiki");
    }else if (b==k && (b>0)){
        printf("boki");
    }else{
        printf("none");
    }
    
    return 0;
}