#include <stdio.h>
#include <math.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    float hyp;
    hyp = pow(b*b+c*c, 0.5);
    
    for (int i=0; i<a; i++){
        int d;
        scanf("%d", &d);
        if (d<=hyp){
            printf("DA\n");
        }else{
            printf("NE\n");
        }
        
    }
    return 0;
}