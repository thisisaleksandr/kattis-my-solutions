#include <stdio.h>

int main(){
    int f=0;
    while(f==0){
        double r, m, c;
        double area, estimate, square;
        scanf("%lf %lf %lf", &r, &m, &c);
        if (r==0 && m==0 && c==0){
            f=1;
            break;
        }
        area = 3.14159265358979323846 * r * r;
        square = r*r*4;
        estimate = square * (float)c/m;
        printf("%.9lf %lf\n", area, estimate);
    }
    return 0;
}