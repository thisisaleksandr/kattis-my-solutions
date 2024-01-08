#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for (int i=0; i<num; i++){
        int store, counter=0;
        scanf("%d", &store);
        int arr[store];
        for (int j=0; j<store; j++){
            scanf("%d", &arr[j]);
        }
        for (int k=0; k<store; k++){
            for (int p=0; p<store-1; p++){
                int x;
                if(arr[p]>arr[p+1]){
                    x = arr[p];
                    arr[p] = arr[p+1];
                    arr[p+1] = x;
                }
            }
        }
        for (int t=1; t<store; t++){
            counter += (arr[t]-arr[t-1]);
        }
        printf("%d\n", counter*2);
    }
    
    return 0;
}