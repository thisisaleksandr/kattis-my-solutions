#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    for (int i=0; i<a; i++){
        int b, c, counter=0;
        scanf("%d %d", &b, &c);
        for(int k=1; k<=c; k++){
            counter+=k;
        }
        printf("%d %d\n", b, counter+c);
    }
    return 0;
}