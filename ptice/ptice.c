#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    char str[num];
    char adr[3] = {'A', 'B', 'C'};
    char bru[4] = {'B', 'A', 'B', 'C'};
    char gor[6] = {'C', 'C', 'A', 'A', 'B', 'B'};
    scanf("%s", str);
    int ad=0, br=0, go=0;
    int x=0, y=0, z=0;
    for(int i = 0; i<num; i++){
        if(i%3==0){
            x = 0;
        }
        if(str[i]==adr[x]){
            ad++;
        }
        x++;
        if(i%4==0){
            y = 0;
        }
        if(str[i]==bru[y]){
            br++;
        }
        y++;
        if(i%6==0){
            z = 0;
        }
        if(str[i]==gor[z]){
            go++;
        }
        z++;
    }
    if(ad>br){
        if(ad>go){
            printf("%d\nAdrian", ad);
        }else if (ad<go){
            printf("%d\nGoran", go);
        }else{
            printf("%d\nAdrian\nGoran", ad);
        }
    }else if(ad<=br){
        if(br>go && ad<br){
            printf("%d\nBruno", br);
        }else if(br<go){
            printf("%d\nGoran", go);
        }else if(br==ad && br==go){
            printf("%d\nAdrian\nBruno\nGoran", br);
        }else if(br==ad){
            printf("%d\nAdrian\nBruno", br);
        }else if(br==go){
            printf("%d\nBruno\nGoran", br);
        }
    }
    return 0;
}