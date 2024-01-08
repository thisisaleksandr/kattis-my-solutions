#include <stdio.h>

int main(){
    int numPhoto;
    scanf("%d", &numPhoto);
    int maxspeed = 0;
    int h, d;
    scanf("%d %d", &h, &d);
    for(int i = 0; i < numPhoto-1; i++){
        int h2, d2;
        scanf("%d %d", &h2, &d2);
        if(((d2-d)/(h2-h))>maxspeed){
            maxspeed = (d2-d)/(h2-h);
        }
        h = h2;
        d = d2;
    }
    printf("%d", maxspeed);
    
    return 0;
}