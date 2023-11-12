#include <stdio.h>

int main(){
    int a;
    scanf("%d", &a);
    for (int i=0; i<a; i++){
        int g, kaka;
        scanf("%d", &g);
        int xyu[g];
        for(int j=0; j<g; j++){
            int code;
            scanf("%d", &code);
            xyu[j]=code;
        }

        for(int k=0; k<g; k++){
            int flag = 0;
            for(int z=0; z<g; z++){
                if (k!=z){
                    if (xyu[k] == xyu[z]){
                        flag=1;
                        //printf("%d", k);
                        break;
                    }
                }
            }
            if (flag==0){
               kaka = xyu[k];
               break;
            }
        }
        printf("Case #%d: %d\n", i+1, kaka);
    }
}