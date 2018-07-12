#include<stdio.h>
int main()
{
	int i,j,n,temp=0,count=0;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
	  count=0;
	  for(j=1;j<i;j++)
	  {
		if(i%j==0)
		{
		   count++;
		}
	  }
	  if(count==1)
	  {
	     if(n%i==0 && i!=n)
	     {
		printf("%d ",i);
	     }
	     if(n%i==0 && i==n)
	     {
		printf("%d",i);
	     }
	  }
	}
	return 0;
}
