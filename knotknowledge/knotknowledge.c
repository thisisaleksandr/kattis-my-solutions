#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    int arr[num];
    
    for(int i=0; i<num; i++){
        scanf("%d", &arr[i]);
    }
    
    int arr2[num-1];
    
    for(int j=0; j<num-1; j++){
        scanf("%d", &arr2[j]);
    }
    
    for(int k=0; k<num; k++){
        int f=0;
        for(int m=0; m<num-1;m++){
            if(arr[k]==arr2[m]){
                f=1;
            }
        }
        if(f==0){
            printf("%d", arr[k]);
            break;
        }
    }
    
    return 0;
}