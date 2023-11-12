#include <stdio.h>
#include <math.h>

int main(){
    int x, y, x1, y1, x2, y2;
    float res;
    scanf("%d %d %d %d %d %d", &x, &y, &x1, &y1, &x2, &y2);
    if(y<=y2 && y>=y1){
        if(x>x2){
            printf("%d", x-x2);
        }else{
            printf("%d", x1-x);
        }
    }else{
        if(x>x2 && y>y2){
            res = pow(((y-y2)*(y-y2) + (x-x2)*(x-x2)), 0.5);
            printf("%f", res);
        }
        else if(x<x1 &&y>y2){
            res = pow(((y-y2)*(y-y2) + (x1-x)*(x1-x)), 0.5);
            printf("%f", res);
        }else if(x>x2 && y<y1){
            res = pow(((y1-y)*(y1-y) + (x-x2)*(x-x2)), 0.5);
            printf("%f", res);
        }else if(x<x1 && y<y1){
            res = pow(((y1-y)*(y1-y) + (x1-x)*(x1-x)), 0.5);
            printf("%f", res);
        }else if(x<=x2 && y>=y2){
            printf("%d", y-y2);
        }else if(y<=y1){
            printf("%d", y1-y);
        }
    }
    return 0;
}