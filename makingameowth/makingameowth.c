#include <stdio.h>

int main(){
    int n, p, x, y;
    scanf("%d %d %d %d", &n, &p, &x, &y);
    int counter = 0, mypage=0;
    while(mypage!=p){
        if(mypage+n-1<=p){
            mypage += n-1;
            counter += ((n-1)*x + y);
        }else{
            counter = counter + (p-mypage)*x;
            mypage += (p-mypage);
        }
    }
    printf("%d", counter);
    
}