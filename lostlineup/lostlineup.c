#include <stdio.h>

int main(){
    int num, k = 2;
    scanf("%d", &num);
    int arr[num];
    arr[0] = 1;
    for(int i=0; i<num-1; i++){
        int people;
        scanf("%d", &people);
        arr[1+people] = k;
        k++;
    }
    for(int j=0; j<num; j++){
        printf("%d ", arr[j]);
    }
    return 0;
}