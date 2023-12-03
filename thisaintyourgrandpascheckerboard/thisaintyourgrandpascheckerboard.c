#include <stdio.h>

int first(char row[][25], int n){
    int flag=1;
    for(int i = 0; i < n; i++){
        int w=0, b=0, consW=0, consB=0;
        for(int j=0; j<n; j++){
            if(row[i][j]=='W'){
                w++;
                consB=0;
                consW++;
                if(consW>=3){
                    flag=0;
                    break;
                }
            }else{
                b++;
                consB++;
                consW = 0;
                if(consB>=3){
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
                consB=0;
                consW++;
                if(consW>=3){
                    flag=0;
                    break;
                }
            }else{
                b++;
                consW=0;
                consB++;
                if(consB>=3){
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