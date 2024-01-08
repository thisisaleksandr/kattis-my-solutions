#include <stdio.h>

int main(){
    int x, y, rad;
    scanf("%d %d", &x, &y);
    scanf("%d", &rad);
    printf("%d %d\n", x-rad, y-rad);
    printf("%d %d\n", x-rad, y+rad);
    printf("%d %d\n", x+rad, y+rad);
    printf("%d %d", x+rad, y-rad);
    
    return 0;
}