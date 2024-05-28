/*
As explained in the comic, consider the following process. Start-
ing from an arbitrary integer n, repeat the following steps:
• If the current number is one, stop.
• If the current number is even, divide it by two (n/2).
• If the current number is odd, triple it and add one (3n+1).
The Collatz conjecture states that this process will always termi-
nate, i.e. the number one is eventually reached. Write a program
that checks the Collatz conjecture for a number given by the
user by applying these rules until 1 is reached.
*/


#include <stdio.h>

int main() {
	int num, steps;

	printf("ENTER A RUNDOM NUMBER TO PLAY COLLATZ: ");
	scanf("%d", &num);

	while (num > 1){
		if (num%2 == 0){
			num /= 2;
		} else {
			num = num * 3 + 1;
		}
		steps += 1;
	}
	printf ("THE NUMBER OF STEPS ARE %d\n", steps);
}
