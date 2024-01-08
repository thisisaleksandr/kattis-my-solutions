#include <stdio.h>
#include <string.h>

int main(){
    int tests;
    scanf("%d", &tests);
    for(int j = 0; j<tests; j++){
        char number[51];
        scanf("%s", number);
        int len, sum=0;
        len = strlen(number);
        if (len%2==0){
            for(int i=0; i<len; i++){
                if(i%2==0){
                    if (((int)(number[i]) - 48) * 2 > 9){
                        sum +=(((int)(number[i]) - 48) * 2) /10 + (((int)(number[i]) - 48) * 2)%10;
                    }else{
                        sum+=((int)(number[i]) - 48) * 2;
                    }
                }else{
                    sum+=(int)(number[i]) - 48;
                }
                
            }
        }else{
            for(int i=0; i<len; i++){
                if(i%2==1){
                    if (((int)(number[i]) - 48) * 2 > 9){
                        sum +=(((int)(number[i]) - 48) * 2) /10 + (((int)(number[i]) - 48) * 2)%10;
                    }else{
                        sum+=((int)(number[i]) - 48) * 2;
                    }
                }else{
                    sum+=(int)(number[i]) - 48;
                }
            }        
        }
        if (sum%10==0){
            printf("PASS\n");
        }else{
            printf("FAIL\n");
        }
    }
    
    return 0;
}