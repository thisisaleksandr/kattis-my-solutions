#include <stdio.h>

int main(){
    char letter;
    scanf("%c", &letter);
    if (letter=='A' || letter=='E' || letter=='I' || letter=='O' || letter=='U'){
        printf("Jebb");
    }else if (letter=='Y'){
        printf("Kannski");
    }else{
        printf("Neibb");
    }
}