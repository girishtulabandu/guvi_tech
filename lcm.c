#include<stdio.h>
int main()
{
	int l,r,i,res=0;
	scanf("%d %d",&l,&r);
	i=r;
	while(i>0)
	{
	   if(i%l==0 && i%r==0)
	   {
		printf("%d",i);
		break;
	   }
	   i++;
	}
	return 0;
}
