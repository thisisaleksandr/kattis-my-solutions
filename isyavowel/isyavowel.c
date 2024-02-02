#include <stdio.h>
#include <string.h>


int main()
{
    char w[51];
    scanf("%s", w);
    
    int len;
    len = strlen(w);
    int vow = 0;
    int y = 0;
    
    for (int i = 0; i < len; i++)
    {

        if ( w[i] == 'a' || w[i] == 'e' || w[i] == 'i' || w[i] == 'o' || w[i] == 'u')
            {
                vow++;
            } 
        else if (w[i] == 'y')
        {

            y++;
        }

    }
    printf("%d %d", vow, vow+y);
    
    return 0;
}
