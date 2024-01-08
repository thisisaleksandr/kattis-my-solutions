#include <stdio.h>

int main(){
    int arr[9];
    int counter=0, left;
    for(int i=0; i<9; i++){
        int num;
        scanf("%d", &num);
        arr[i] = num;
        counter+=num;
    }
    left=counter-100;
    int num1ind, num2ind;
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            if (arr[i] + arr[j] == left && i!=j){
                num1ind = i;
                num2ind = j;
                break;
            }
        }
    }
    
    for(int i=0; i<9; i++){
        if(i!=num1ind && i!=num2ind){
            printf("%d\n", arr[i]);
        }
    }
    
    
    return 0;
    
}