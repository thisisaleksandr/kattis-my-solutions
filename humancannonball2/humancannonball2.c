#include <stdio.h>
#include <math.h>
int main(){
    int num;
    scanf("%d", &num);
    float g=9.81;
    for(int i=0; i<num; i++){
        float v, o, x, h1, h2, t, y;
        scanf("%f %f %f %f %f", &v, &o, &x, &h1, &h2);
        t = (float)x/(v*cos(o*3.14159265/180));
        y = v*t*sin(o*3.14159265/180)-(float)(g*pow(t, 2))/2;
        if(y >= h1+1 && y <= h2-1){
            printf("Safe\n");
        }else{
            printf("Not Safe\n");
        }
    }
    
    return 0;
}