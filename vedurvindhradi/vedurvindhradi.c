#include <stdio.h>

int main(){
    double s;
    scanf("%lf", &s);
    if (0 <= s && s <= 0.29){
        printf("Logn");
    }
    if (0.3 <= s && s <= 1.59){
        printf("Andvari");
    }
    if (1.6 <= s && s <= 3.39){
        printf("Kul");
    }
    if (3.4 <= s && s <= 5.49){
        printf("Gola");
    }
    if (5.5 <= s && s <= 7.99){
        printf("Stinningsgola");
    }
    if (8.0 <= s && s <= 10.79){
        printf("Kaldi");
    }
    if (10.8 <= s && s <= 13.89){
        printf("Stinningskaldi");
    }
    if (13.9 <= s && s <= 17.19){
        printf("Allhvass vindur");
    }
    if (17.2 <= s && s <= 20.79){
        printf("Hvassvidri");
    }
    if (20.8 <= s && s <= 24.49){
        printf("Stormur");
    }
    if (24.5 <= s && s <= 28.49){
        printf("Rok");
    }
    if (28.5 <= s && s <= 32.69){
        printf("Ofsavedur");
    }
    if (32.7 <= s){
        printf("Farvidri");
    }    
    return 0;
}