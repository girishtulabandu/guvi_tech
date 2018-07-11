#include<stdio.h>
#include<stdlib.h>
int main()
{
	long int arr[20],i,j,n,count=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	   scanf("%ld",&arr[i]);
	}
	
	for(i=0;i<n;i++)
	{
	  count=0;
	  for(j=0;j<n;j++)
	   {
		if(arr[i]==arr[j])
		{
		   count++;
		}
	
	   }
	   
	   if(count==1)
	   {
		printf("%ld",arr[i]);
	   }
	    
	}

	return 0;
	
}
