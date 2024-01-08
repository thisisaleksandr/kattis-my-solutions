#include <stdio.h>
int c=0;

long long int ipow(long long int a, unsigned int n)
{
    if(n==0)
        return 0;
    if(n==1)
        return a;
    if(n%2==0){
        //(*depth)++;
        c++;
        return ipow(a, n/2) * ipow(a, n/2);
    }else{
        c++;
        //(*depth)++;
        return a * ipow(a, n-1);
    }
}

int main(){
    
    int d = 7, res;
    res = ipow(2, 32);  // res = 4294967296, d = 6
    res = ipow(3, 12);  // res = 531441, d = 5
    printf("%d %d\n", res, c);
    
    return 0;
}
    