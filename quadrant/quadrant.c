#include <stdio.h>


int main(){
   int num1, num2;
   scanf("%d", &num1);
   scanf("%d", &num2);
   if (num1>0){
       if (num2>0){
           printf("%d", 1);
       }else{
           printf("%d", 4);
       }
   }else{
       if (num2>0){
           printf("%d", 2);
       }else{
           printf("%d", 3);
       }
   }
   return 0;
}