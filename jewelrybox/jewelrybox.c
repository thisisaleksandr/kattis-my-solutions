#include <stdio.h>
#include <math.h>

int main(){
    int tests;
    scanf("%d", &tests);
    for(int i=0; i<tests; i++){
        int x, y, area, a, b;
        double volume, h;
        scanf("%d %d", &x, &y);
        h = (double)(4*(x+y) - pow(16*(x+y)*(x+y) - 48*x*y, 0.5))/24;
        volume = (x-2*h)*(y-2*h)*h;
        printf("%.11lf\n", volume);
    }
    
    return 0;
}