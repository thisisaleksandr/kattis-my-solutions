#include <stdio.h>

int main(){
    int a, c=0;
    scanf("%d", &a);
    int arr[a][a];
    int z;
    for(int i=0; i<a; i++){
        for(int j=0; j<a; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    for(int i=0; i<a; i++){
        for(int j=0; j<a; j++){
            if (arr[i][j] != -1){
                c++;
            };
        }
    }
    printf("%d\n", c);
    
    for(int i=0; i<a; i++){
        for(int j=0; j<a; j++){
            if (arr[i][j] != -1){
                printf("%d %d %d\n", i+1, j+1, arr[i][j]);
            }
        }
    }    
    
    return 0;
}