#include<stdio.h>
int main()
{
	int arr[20],i,j,n,k,temp;
	scanf("%d %d",&n,&k);
	for(i=0;i<n;i++)
	{
	   scanf("%d",&arr[i]);
	}
	
	for(i=0;i<n;i++)
	{
	   for(j=i+1;j<n;j++)
	   {
		if(arr[i]<arr[j])
		{
		temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
		}
	   }
	}

	printf("%d",arr[k-1]);
	return 0;
}
