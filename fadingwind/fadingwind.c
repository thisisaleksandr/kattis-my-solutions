#include <stdio.h>

int main(){
    int h, k, v, s, vmax, c=0;
    scanf("%d %d %d %d", &h, &k, &v, &s);
    
    while (h>0){
        v = v+s;
        vmax = v/10;
        if (vmax ==0){
            v = v - 1;
        }else{
            v = v - vmax;
        }
        if (v >= k){
            h++;
        }else if (v < k && v > 0){
            h--;
            if (h==0){
                v = 0;
            }
        }else if (v <= 0){
            h = 0;
            v = 0;
        }
        c += v;
        if (s>0){
            s--;
        }
    }
    printf("%d", c);
    
    return 0;
}