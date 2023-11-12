#include <stdio.h>

int main(){
    int num, counter=0;
    scanf("%d", &num);
    for(int i = 0; i < num; i++){
        int prize;
        scanf("%d", &prize);
        counter += prize;
    }
    if(counter%3==0){
        printf("yes");
    }else{
        printf("no");
    }
    
    return 0;
}