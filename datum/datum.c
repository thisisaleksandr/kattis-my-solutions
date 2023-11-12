#include <stdio.h>

int main(){
    int d, m;
    scanf("%d %d", &d, &m);
    if(m==1||m==10){
        d+=4;
    }
    if(m==4||m==7){
        d+=3;
    }    
    if(m==5){
        d+=5;
    } 
    if(m==6){
        d+=6;
    }   
    if(m==8){
        d+=6;
    } 
    if(m==9||m==12){
        d+=2;
    }   
    
    if (d%7==1){
        printf("Sunday");
    }
    if (d%7==2){
        printf("Monday");
    }
    if (d%7==3){
        printf("Tuesday");
    }
    if (d%7==4){
        printf("Wednesday");
    }
    if (d%7==5){
        printf("Thursday");
    }
    if (d%7==6){
        printf("Friday");
    }    
    if (d%7==0){
        printf("Saturday");
    }        
    return 0;
}