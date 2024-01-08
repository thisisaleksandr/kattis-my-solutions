#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    while (1){
        double x1, y1, x2, y2, p, dist;
        scanf("%lf", &x1);
        if (x1==0.0){
            break;
        }
        scanf(" %lf %lf %lf %lf", &y1, &x2, &y2, &p);

        dist = pow((pow(fabs(x1-x2), p) + pow(fabs(y1-y2), p)), (double)(1/p));
        
        printf("%.10f\n", dist);
    }
    return 0;
}