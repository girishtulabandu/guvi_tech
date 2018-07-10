#include<stdio.h>
int main()
{
	int arr[20],arr1[20],i,j=-1,n,count=0,temp=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	   scanf("%d",&arr[i]);
	}
	
	for(i=0;i<n;i++)
	{
	  if(arr[i]==i)
	  {
		if(temp==0)
		{
			printf("%d",arr[i]);
			temp++;
		}
		else
		{
			printf(" %d",arr[i]);
		}
	  }
	   
	
	}
	

	
	return 0;
}
