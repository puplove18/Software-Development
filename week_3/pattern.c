/*
Write a program that prints an pyramid pattern of n rows, where n is given by the user.
Example:
Tobias Meggendorfer – Michaelmas Term 2023/24
> Enter number of rows: 5
>      *
>     ***
>    *****
>   *******
>  *********
*/


#include <stdio.h>

int main() {
	int rows, start = 1;
	
	printf("ENTER NUMBER OF THE ROWS HERE: ");
	scanf("%d", &rows);

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < rows - i - 1; j++) {
			printf(" ");
		}
		for (int k = 0; k < 2 * i + 1; k++) {
			printf ("*");
		}

		printf ("\n");
	}
	return 0;
}
