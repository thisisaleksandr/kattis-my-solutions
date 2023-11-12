#include <stdio.h>

void printOutput(int fizz, int buzz, int num){

    for(int i=1; i<=num; i++){
        if(i%fizz == 0 && i%buzz==0){
            printf("FizzBuzz\n");
        }else if(i%buzz==0){
            printf("Buzz\n");
        }else if(i%fizz==0){
            printf("Fizz\n");
        }else{
            printf("%d\n", i);
        }
    }
}

int main(){

    int fizz, buzz, num;

    scanf("%i %d %d", &fizz, &buzz, &num);

    printOutput(fizz, buzz, num);

    return 0;
}
