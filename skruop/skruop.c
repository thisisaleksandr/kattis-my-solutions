#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    int level = 7;
    while(getchar()!='\n');
    for(int i=0; i<num; i++){
        char str[9];
        //fgets(str, 9, stdin);
        gets(str);
        if (str[5]=='o' && level<10){
            level++;
        }
        if (str[5]=='n' && level>0){
            level--;
        }
        //printf("%s\n", str);
    }
    printf("%d", level);
    
    return 0;
}