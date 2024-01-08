#include <stdio.h>

int main(){
    char str[51];
    int ball=1, i=0;
    scanf("%s", str);
    
    while(str[i] != '\0'){
        if (ball == 1){
            if (str[i] == 'A'){
                ball = 2;
            }else if (str[i] == 'C'){
                ball = 3;
            }
        }else if (ball == 2){
            if (str[i] == 'A'){
                ball = 1;
            }else if (str[i]=='B'){
                ball = 3;
            }
        }else if (ball==3){
            if (str[i] == 'C'){
                ball = 1;
            }else if (str[i]=='B'){
                ball = 2;
            }
        }
        i++;
    }
    printf("%d", ball);
    return 0;
}