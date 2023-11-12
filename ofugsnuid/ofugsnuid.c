#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    int arr[num];
    for(int i=0; i<num; i++){
        scanf("%d", &arr[i]);
    }
    for(int j=num-1; j>=0; j--){
        printf("%d\n", arr[j]);
    }    
    return 0;
}