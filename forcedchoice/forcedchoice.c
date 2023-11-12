#include <stdio.h>

int main() {
    int n, p, s;
    scanf("%d %d %d", &n, &p, &s);
    for(int i=0; i<s; i++){
        int cards, f=0;
        scanf("%d", &cards);
        for(int j=0; j<cards; j++){
            int card;
            scanf("%d", &card);
            if (card==p){
                f=1;
            }
        }
        if (f==1){
            printf("KEEP\n");
        }else{
            printf("REMOVE\n");
        }
    }
    return 0;
}