/*
The Fibonacci numbers are defined by a1 = a2 = 1 and ai = ai≠1 + ai≠2, i.e. the ith number is the sum of
the two previous ones. Write a program that reads a number n from the user and prints the nth Fibonacci
number.
For reference: The first Fibonacci numbers are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144. Check that your
program returns the correct values, also for n = 1 or n = 2.
*/

#include <stdio.h>

int main() {
  int n, a = 1, b = 1;

  printf("ENTER THE NUMBER TO FIND YOUR FIBONACCI NUNBER: ");
	scanf("%d", &n);

  for (int i =2; i < n; i++) {

    b += a;
    a = b - a;

  }
	printf("YOUR %dTH FIBONACCI NUMBER IS %d\n", n, b);
	
	return 0;
}
