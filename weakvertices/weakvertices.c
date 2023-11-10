#include <stdio.h>

int main(){
    int f=1;
    while(f!=0){
        int num;
        scanf("%d", &num);
        if(num==-1){
            f=0;
            break;
        }
        int arr[num][num];
        
        for(int i=0; i<num; i++){
            for(int j=0; j<num; j++){
                scanf("%d", &arr[i][j]);
            }
        }
        
        for(int i = 0; i < num; i++) {
            int weak = 1;
            for(int j = 0; j < num; j++) {
                for(int k = 0; k < num; k++) {
                    if(arr[i][k]==1 && arr[i][j]==1 && arr[j][k]==1 && i!=k && i!=j && j!=k) {
                        weak = 0;
                    }
                }
            }

            if(weak==1) {
                printf("%d ", i);
            }
        }
        printf("\n");
        
    }
}