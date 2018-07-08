#include<stdio.h>
int main()
{
	int arr[20],i,n,min=9999;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	   scanf("%d",&arr[i]);
	}
	for(i=0;i<n;i++)
	{
	   if(arr[i]<min)
	   {
		min=arr[i];
	   }
	}
	printf("%d",min);
	return 0;
	
}
