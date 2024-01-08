#include <stdio.h>

int main(){

    int numCases, j=0;


    scanf("%i", &numCases);

    for(int i=0; i<numCases; i++){
        j=0;
        char str1[51], str2[51];
        scanf("%s", str1);
        scanf("%s", str2);
        printf("%s\n", str1);
        printf("%s\n", str2);

        while(str1[j] != '\0'){
            if(str1[j]==str2[j]){
                printf(".");
            }else{
                printf("*");
            }
            j++;
        }
        printf("\n\n");
    }


    return 0;
}
