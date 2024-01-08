#include <stdio.h>
#include <string.h>

int main() {
    char str[16];
    scanf("%s", str);
    for(int k=0; k<5; k++){
        int j=0;
        if (k!=2){
            while (j<strlen(str)){
                if (j%3!=0 || j==0){
                    if ((j+1)%3!=0){
                        if (k==0 || k==4){
                            printf("..#.");
                        }else{
                            printf(".#.#");
                        }
                    }else {
                        if (k==0 || k==4){
                            printf("..*..");
                        }else{
                            printf(".*.*.");
                        }
                    }
                }else{   //j%3==0 posle 3 bukvy #
                    if (k==0 || k==4){
                        printf(".#.");
                    }else{
                        printf("#.#");
                    }
                }
                j++;
                if (j==strlen(str) && j%3!=0){
                        printf(".");
                }
            }
        }else{
            while(j<strlen(str)){
                if (j%3 != 0 || j==0){
                    if ((j+1)%3!=0){
                        printf("#.%c.", str[j]);
                    }else {
                        printf("*.%c.*", str[j]);
                    }
                }else{ //j%3==0
                    printf(".%c.", str[j]);
                }
                j++;
                if (j==strlen(str) && j%3!=0){
                        printf("#");
                }                
            }
        }
        printf("\n");
    }
    return 0;
}