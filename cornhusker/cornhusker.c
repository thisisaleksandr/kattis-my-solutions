#include <stdio.h>

int main(){
    int arr[10], a, b, av_num=0, bushel;
    for(int i=0; i<10; i++){
        scanf("%d", &arr[i]);
    }
    scanf("%d %d", &a, &b);
    for(int j=0; j<9; j+=2){
        av_num+=(arr[j]*arr[j+1]);
    }
    av_num/=5;
    bushel = (a*av_num)/b;
    printf("%d", bushel);
    
    return 0;
}