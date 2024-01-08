#include <stdio.h>

int main(){
    
    int a;
    int cpu=0, ws=0, mem=0;
    scanf("%d", &a);
    for (int i=0; i<a; i++){
        char c, w, m;
        scanf(" %c %c %c", &c, &w, &m);
        if (c=='J'){
            cpu++;
        }
        if (w=='J'){
            ws++;
        }
        if (m=='J'){
            mem++;
        }
    }
    if (cpu <= ws){
        if (cpu <= mem){
            printf("%d", cpu);
        }else if (mem < cpu){
            printf("%d", mem);
        }
    }else if(ws<cpu){
        if (ws<=mem){
            printf("%d", ws);
        }else if(mem<ws){
            printf("%d", mem);
        }
    }
    return 0;
}