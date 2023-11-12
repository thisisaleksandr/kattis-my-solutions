#include <stdio.h>

int main(){
    int s, t, n, counter=0;
    scanf("%d %d %d", &s, &t, &n);
    int arr[n], arr2[n], arr3[n];
    for (int i=0; i <= n; i++){
        int d;
        scanf("%d", &d);
        arr[i] = d;
    }
    for (int i=0; i < n; i++) {
        int b;
        scanf("%d", &b);
        arr2[i] = b;
    }
    for (int i=0; i < n; i++) {
        int c, x;
        scanf("%d", &c);
        arr3[i] = c;
        if (c > counter+arr[i]) {
            x = c-(counter+arr[i]);
        }else{
            x = (counter+arr[i])%c;
        }
        counter += arr[i] + x + arr2[i];
    }
    counter+=arr[n];
    
    if (counter <= t-s){
        printf("yes");
    }else{
        printf("no");
    }
    
    return 0;
}