#include <stdio.h>

int main(){
    int a, b, c, g, s, sum;
    scanf("%d %d %d", &a, &b, &c);
    g = a*3;
    s = b*2;
    sum = g+s+c;
    if(sum>=8){
            printf("Province or Gold");
            sum-=8;
    }else if (sum >=6){
            printf("Duchy or Gold");
            sum -= 5;
    }else if (sum>=5){
            printf("Duchy or Silver");
    }else if (sum>=3){
            printf("Estate or Silver");
            sum-=5;
    }else if (sum>=2){
            printf("Estate or Copper");
            sum-=5;
    }else{
            printf("Copper");
            sum-=5;
    }
    return 0;
}