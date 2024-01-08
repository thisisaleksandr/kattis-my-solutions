#include <stdio.h>

int main(){
    char arr[3][3];
    for(int i=0; i<3; i++){
        scanf(" %c %c %c", &arr[i][0], &arr[i][1], &arr[i][2]);
    }
    int ac=0, jc=0;
    for(int i=0; i<3; i++){
        if (arr[i][0] == arr[i][1] && arr[i][1] == arr[i][2]){
            if(arr[i][0] == 'X'){
                jc = 3;
            }else if(arr[i][0]=='O'){
                ac = 3;
            }
        }
    }
    for(int i=0; i<3; i++){
        if (arr[0][i] == arr[1][i] && arr[1][i] == arr[2][i]){
            if(arr[0][i]=='X'){
                jc = 3;
            }else if(arr[0][i]=='O'){
                ac = 3;
            }
        }
    }
    if(arr[0][0]==arr[1][1] && arr[1][1] ==arr[2][2] || arr[0][2]==arr[1][1]&&arr[1][1]==arr[2][0]){
            if(arr[1][1]=='X'){
                jc = 3;
            }else if (arr[1][1]=='O'){
                ac = 3;
            }
    }
    if(jc==3){
        printf("Johan har vunnit");
    }else if(ac==3){
        printf("Abdullah har vunnit");
    }else{
        printf("ingen har vunnit");
    }

    return 0;
    
}