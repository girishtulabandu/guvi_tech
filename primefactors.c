#include <stdio.h>

int isPrime(int num)
{
	for (int i = 2; i * i <= num; i++)
		if (num % i == 0)
			return 0;
	return 1;
}

void primeFactors(int n)
{
	for (int i = 2; i * i < n; i++)
		if (n % i == 0)
			if (isPrime(i))
				printf("%d ", i);
}

int main()
{
	int n;
	scanf("%d", &n);
	primeFactors(n);
	return 0;
}
