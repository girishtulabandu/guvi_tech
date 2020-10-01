#include<stdio.h>
int main()
{
	int arr[20],i,n,max=-9999;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	   scanf("%d",&arr[i]);

	   if(arr[i]>max)
	   {
		max=arr[i];
	   }
	}
	printf("%d",max);
	return 0;
}
