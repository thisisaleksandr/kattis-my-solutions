#include <stdio.h>

int main(){
    int a1,b1,a2,b2;
    float gun;
    scanf("%d %d %d %d", &a1, &b1, &a2, &b2);
    gun = (float)(a1+b1)/2 + (float)(a2+b2)/2;
    
    int c1,d1,c2,d2;
    float emma;
    scanf("%d %d %d %d", &c1, &d1, &c2, &d2);
    emma = (float)(c1+d1)/2 + (float)(c2+d2)/2;
    
    if (gun>emma){
        printf("Gunnar");
    }else if (emma>gun){
        printf("Emma");
    }else{
        printf("Tie");
    }
}