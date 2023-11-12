#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for(int i=0; i< num; i++){
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        if (a+b==c || a*b==c || (float)a/b==c || a-b==c){
            printf("Possible\n");
        }else if ((float)b/a==c || b-a==c){
            printf("Possible\n");
        }else{
            printf("Impossible\n");
        }
    }
    
    return 0;
}