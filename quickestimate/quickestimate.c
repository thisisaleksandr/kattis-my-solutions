#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){
    int num;
    scanf("%d", &num);
    //int x;
    //x = pow(10, 100);
    for(int i=0; i<num; i++){
        char str[100000];
        scanf("%s", str);
        printf("%d\n", strlen(str));
    }
    return 0;
}