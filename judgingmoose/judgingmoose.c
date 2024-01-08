#include <stdio.h>

int main(){
    int l, r;
    scanf("%d %d", &l, &r);
    if (l==r && l!=0){
        printf("Even %d", l+r);
    }else if (l>r || r>l){
        if(l>r){
            printf("Odd %d", l*2);
        }else{
            printf("Odd %d", r*2);
        }
    }else {
        printf("Not a moose");
    }
}