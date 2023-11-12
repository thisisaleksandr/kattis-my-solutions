#include <stdio.h>

int main(){
    int a, b, counter=0;
    scanf("%d %d", &a, &b);
    int arr[a];
    for(int i=0; i<a; i++){
        scanf("%d", &arr[i]);
    }
    for(int j=0; j<a; j++){
        if(b>=arr[j]){
            b-=arr[j];
            counter++;
        }else{
            break;
        }
    }
    printf("%d", counter);
    
    return 0;
    
}