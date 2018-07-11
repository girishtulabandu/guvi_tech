#include<stdio.h>
int main()
{
  int i,n,ans=0,rem;
  scanf("%d",&n);
  while(n>0)
  {
	rem=n%10;
	n=n/10;
	ans=ans+(rem*rem);	
  }
  printf("%d",ans);
  return 0;
}
