#include <stdio.h>

int main(){
    int a;
    float b;
    scanf("%d", &a);
    for (int i = 0; i < a; i++){
        int dist;
        scanf("%d", &dist);
        switch (dist) {
            case 2:
            case 12:
                dist = 1;
                break;
            case 3:
            case 11:
                dist = 2;
                break;
            case 4:
            case 10:
                dist = 3;
                break;
            case 5:
            case 9:
                dist = 4;
                break;
            case 6:
            case 8:
                dist = 5;
                break;
            case 7:
                dist = 6;
                break;
            default:
                dist = 0;
        }
        b += (float)dist/36;
    }
    printf("%f", b);
    return 0;
}