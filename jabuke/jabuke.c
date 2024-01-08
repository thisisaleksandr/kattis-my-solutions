#include <stdio.h>
#include <stdlib.h>

float area(int xa, int ya, int xb, int yb, int xc,  int yc){
    float area;
    area = (float)(abs(xa*(yb-yc) + xb*(yc-ya) + xc*(ya-yb)))/2;
    return area;
}

int main(){
    int xa, ya, xb, yb, xc, yc;
    scanf("%d %d", &xa, &ya);
    scanf("%d %d", &xb, &yb);
    scanf("%d %d", &xc, &yc);
    int num, counter=0;
    float main_area;
    main_area = area(xa, ya, xb, yb, xc, yc);
    scanf("%d", &num);
    for(int i=0; i<num; i++){
        int x, y;
        scanf("%d %d", &x, &y);
        float a, b, c;
        a = area(x, y, xb, yb, xc, yc);
        b = area(xa,ya,x,y,xc,yc);
        c = area(xa,ya,xb,yb,x,y);

        if (a+b+c == main_area){
            counter++;
        }
    }
    printf("%.1f\n%d", main_area, counter);
    
    return 0;
}
