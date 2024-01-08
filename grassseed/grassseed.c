#include <stdio.h>

int main() {
    int l;
    float c, counter=0;
    scanf("%f", &c);
    scanf("%d", &l);
    for (int i = 0; i<l; i++){
        float a, b;
        scanf("%f%f", &a, &b);
        float sow;
        sow = a*b*c;
        counter += sow;
    }
    printf("%f", counter);
    
    return 0;
}