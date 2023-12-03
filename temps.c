#include <stdio.h>
//WBBW
//WBWB
//BWWB
//BWBW

int first(char row[][25], int n){
    int flag=1;
    for(int i = 0; i < n; i++){
        int w=0, b=0, consW=0, consB=0;
        for(int j=0; j<n; j++){
            if(row[i][j]=='W'){
                w++;
                if(consW<3){
                    consB=0;
                    consW++;
                }else{
                    flag=0;
                    break;
                }
            }else{
                b++;
                if(consB<3){
                    consW=0;
                    consB++;
                }else{
                    flag=0;
                    break;
                }                
            }
        }
        if(w!=b){
            flag=0;
            break;
        }
    }
    return flag;
}

int second(char col[][25], int n){
    int flag = 1;
    for(int i = 0; i < n; i++){
        int w=0, b=0, consW=0, consB=0;
        for(int j=0; j<n; j++){
            if(col[j][i]=='W'){
                w++;
                if(consW<3){
                    consB=0;
                    consW++;
                }else{
                    flag=0;
                    break;
                }
            }else{
                b++;
                if(consB<3){
                    consW=0;
                    consB++;
                }else{
                    flag=0;
                    break;
                }                
            }
        }
        if(w!=b){
            flag=0;
            break;
        }
    }
    return flag;    
}


int main(){
    int n;
    scanf("%d", &n);
    char str[n][25];
    for(int i = 0; i < n; i++){
        scanf("%s", str[i]);
    }
    
    if(first(str, n) + second(str, n) == 2){
        printf("1");
    }else{
        printf("0");
    }
    
    
    return 0;
}