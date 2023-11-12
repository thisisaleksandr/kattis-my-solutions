#include <stdio.h>

int func(int num){
    int n1, n2, n3, n4, n5, n6;
    n1 = num/100000;
    n2 = (num/10000)%10;
    n3 = (num/1000)%10;
    n4 = (num/100)%10;
    n5 = (num/10)%10;
    n6 = num%10;
    if ((n1!=n2 && n2!=n3 && n3!=n4 && n4!=n5 && n5!=n6 && n1!=n3 && n1!=n4 &&n1!=n5&&n1!=n6&&n2!=n3&&n2!=n4&&n2!=n5&&n2!=n6&&n3!=n5&&n3!=n6&&n4!=n6)&&(n1*n2*n3*n4*n5*n6>0)){
        if (num%n1==0 && num%n2==0 && num%n3==0
        && num%n4==0 && num%n5==0 && num%n6==0){
            return 1;
        }else{
            return 0;
        }
    }else{
        return 0;
    }
}

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    int counter = 0;
    for(int i=a; i<=b; i++){
        counter += func(i);
    }
    printf("%d", counter);
    return 0;
}