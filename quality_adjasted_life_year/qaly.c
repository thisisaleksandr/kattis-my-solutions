#include <stdio.h>

int main(){
    int num;
    float counter=0;
    scanf("%d", &num);
    for(int i=0; i<num; i++){
        float qual, years;
        scanf("%f %f", &qual, &years);
        counter+=qual*years;
    }
    printf("%.3f", counter);
}