#include <stdio.h>

int main(){
    
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    for(int k=1; k<n; k++){
        int x = arr[0], j=1, v=2;
        while(x%arr[k]!=0){
            x=arr[0]*v;
            j++;
            v++;
        }
        printf("%d/%d\n", x/arr[k], j);
    }
    return 0;
}