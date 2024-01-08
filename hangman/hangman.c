#include <stdio.h>
#include <string.h>

int main(){
    char word[17];
    char perm[27];
    int tries = 10, lenword, counter=0;
    scanf("%s", word);
    scanf("%s", perm);
    for(int i=0; i<strlen(perm); i++){
        int flag=0;
        for(int j=0; j<strlen(word); j++){
            if(perm[i] == word[j]){
                counter+=1;
                flag=1;
            }
        }
        if(flag==0){
            tries--;
            if(tries==0){
            printf("LOSE");
            break;
            }
        }
        if(counter==strlen(word)){
            printf("WIN");
            break;
        }
    } 
}