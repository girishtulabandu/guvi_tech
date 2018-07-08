#include<stdio.h>
int main()
{
	int arr[20],i,j,n,temp=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	   scanf("%d",&arr[i]);
	}
	
	for(i=0;i<n;i++)
	{
	   
	   for(j=i+1;j<n;j++)
	   {
		if(arr[i]>arr[j])
		{
		   temp=arr[j];
		   arr[j]=arr[i];
		   arr[i]=temp;
		}
	   }
	}
	
	for(i=0;i<n;i++)
	{
	   if(i!=n)
	   {
	   printf("%d ",arr[i]);
	   }
	   if(i==n)
	   {
		printf("%d",arr[i]);
	   }

	}
	return 0;
}
