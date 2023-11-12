#include <stdio.h>
#include <math.h>

int main(){
    int a, b, counter = 0;
    scanf("%d", &a);
    scanf("%d", &b);
    if(a/1000 != b/1000){
        counter++;
    }
    if(a/100%10 != b/100%10){
        counter++;
    }
    if(a/10%10 != b/10%10){
        counter++;
    }
    if(a%10 != b%10){
        counter++;
    }
    //printf("%d", counter);
    int ans = pow(2, counter);
    printf("%d", ans);
    
    return 0;
}