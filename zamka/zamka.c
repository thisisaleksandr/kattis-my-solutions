#include <stdio.h>

int main() {
    
    int l, d, x, counter=0;
    scanf("%d", &l);
    scanf("%d", &d);
    scanf("%d", &x);
    
    for(int i=l; i<=d; i++){
        int c=0, z;
        z = i;
        while (z!=0){
            c+=z%10;
            z=z/10;
        }
        if (c==x){
            printf("%d\n", i);
            break;
        }
    }
    for(int i=d; i>=l; i--){
        int c=0, z;
        z = i;
        while (z!=0){
            c+=z%10;
            z=z/10;
        }
        if (c==x){
            printf("%d", i);
            break;
        }
    }    
    return 0;
}