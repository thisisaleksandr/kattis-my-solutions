#include <stdio.h>

int main(){
    int flag = 0;
    while(flag==0){
        int num;
        scanf("%d", &num);
        if (num==-1){
            flag=1;
            break;
        }
        int counter=0;
        int z = 0;
        for(int i=0; i<num; i++){
            int a, b;
            scanf("%d %d", &a, &b);
            counter += (a*(b-z));
            z = b;
        }
        printf("%d miles\n", counter);
    }
}
