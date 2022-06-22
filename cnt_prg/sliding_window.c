#include<stdio.h>
int main()
{
    int f,w,frames[50],i;
    printf("Window Size");
    scanf("%d",&w);
    printf("No of Frames");
    scanf("%d",&f);
    for(i=1;i<=f;i++)
    scanf("%d",&frames[i]);
    for(i=1;i<=f;i++)
    {
        if(i%w==0)
        {
            printf("%d ",frames[i]);
            printf("ACK BY SENDER\n");
        }
        else
        printf("%d ",frames[i]);
    }
    if(f%w!=0)
    printf("ACK BY RECEIVER");
    return 0;
}