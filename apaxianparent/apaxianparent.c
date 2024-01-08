#include <stdio.h>
#include <string.h>

int main(){
    char arra[11], arrb[11];
    int leng, lengb;
    scanf("%s", arra);
    scanf("%s", arrb);
    
    leng = strlen(arra);

    if (arra[leng-1] == 'e'){
        printf("%sx%s", arra, arrb);
    }else if (arra[leng-1] == 'a' || arra[leng-1] == 'i'
            || arra[leng-1] == 'o' || arra[leng-1] == 'u'){
        arra[leng-1] = '\0';
        printf("%sex%s", arra, arrb);
    }else if (arra[leng-2] == 'e' && arra[leng-1] == 'x'){
        printf("%s%s", arra, arrb);
    }else{
        printf("%sex%s", arra, arrb);
    }
    return 0;
}