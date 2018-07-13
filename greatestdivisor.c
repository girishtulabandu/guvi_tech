#include<stdio.h>
int main()
{
	int n,k,r,i,total=0;
	scanf("%d %d",&n,&k);
	if(n>k)
	r=n;
	else
	r=k;
	for(i=1;i<=r;i++)
	{
	   if(n%i==0 && k%i==0)
	   {
		total=i;
	   }
	}
	printf("%d",total);
	
}
