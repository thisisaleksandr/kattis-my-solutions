#include <stdio.h>

int main(){
    int num, emp;
    scanf("%d", &num);
    int arr[num], sarr[num];
    for(int i=0; i<num; i++){
        if (i!=num-1){
            scanf("%d ", &arr[i]);
        }else{
            scanf("%d", &arr[i]);
        }
    }
    
    for(int i=0; i<num; i++){
        for(int j=0; j<num; j++){
            if (arr[j]<arr[j+1]){
                int temp;
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    int maxnum = arr[0], minnum = arr[-1], counter=0;
    for(int i=1; i<=num; i++){
        if(arr[i]+i > counter){
            counter=(arr[i]+i);
            
        }
    }
    printf("%d\n", counter+1);
    return 0;
}