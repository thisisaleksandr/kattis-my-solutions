#include <stdio.h>

int main(){
    while (1){
        int maxwidth, mywidth=0, myheight=0, genh=0, genw=0;
        scanf("%d", &maxwidth);
        if (maxwidth == 0){
            break;
        }
        while (1){
            int x, y;
            scanf("%d %d", &x, &y);
            if (x==-1){
                break;
            }
            if (mywidth+x <= maxwidth){
                mywidth+=x;
                if (y>myheight){
                    myheight=y;
                }
            }else{
                if (mywidth > genw){
                    genw=mywidth;
                }
                genh+=myheight;
                mywidth = x;
                myheight = y;
            }
        }
        if (mywidth > genw){
            genw=mywidth;
        }   
        genh+=myheight;
        printf("%d x %d\n", genw, genh);
    }
    return 0;
}