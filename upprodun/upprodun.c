#include <stdio.h>

int main(){
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    int c=n;
    for(int i=0; i<c; i++){
        int ppl_room;
        ppl_room = m/n;
        for(int j=0; j<ppl_room; j++){
            printf("*");
        }
        m = m - ppl_room;
        n = n -1;
        printf("\n");
    }
}