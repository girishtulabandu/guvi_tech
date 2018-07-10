#include<stdio.h>
#include<stdlib.h>
int main()
{
	int arr[20],i,j,n;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	   scanf("%d",&arr[i]);
	}
	
	for(i=0;i<n;i++)
	{
	  for(j=i+1;j<n;j++)
	   {
		if(arr[i]==arr[j])
		{
		   printf("%d",arr[i]);
		   exit(0);
		}
	
	   }
	   
	}
	return 0;
	
}
