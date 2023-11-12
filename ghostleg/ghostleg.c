#include <stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    int arr[b];
    for(int i=0; i<b; i++){
        scanf("%d", &arr[i]);
    }
    for(int j=1; j<=a; j++){
        int pos;
        pos = j;
        for(int k=b-1; k>=0; k--){
            if (arr[k]==pos){
                pos=arr[k]+1;
            }else if (arr[k]==pos-1){
                pos=arr[k];
            }
        }
        printf("%d\n", pos);
    }
    return 0;
}