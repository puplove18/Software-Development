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
