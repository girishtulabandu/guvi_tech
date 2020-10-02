#include<stdio.h>
int main()
{
	// This code takes a list of numbers and reorders them largest to smallest
	int arr[20],i,j,n,temp=0;
	scanf("%d",&n); // How many values to read
	for(i=0;i<n;i++)
	{
	   scanf("%d",&arr[i]); // Enter in the values one by one.
	}
	
	for(i=0;i<n;i++)
	{
	   
	   for(j=i+1;j<n;j++)
	   {
		if(arr[i]<arr[j])
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
  	   	printf("%d,",arr[i]);
	   }
	   else
	   {
		printf("%d\n",arr[i]);
	   }

	}
	return 0;
}
