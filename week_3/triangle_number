/*
The Nth triangular number is the sum of all numbers from 1 to n. 
Write a program that reads n from the user and outputs the nth triangular number, using a for-loop.
*/

#include <stdio.h>

int main(){
  int n, sum = 0;
  do{
    printf("Enter a positive number: ");
    if (!scanf("%d", &n)) {scanf("%*s); continue;}
  } while (n <= 0);

  for (int i = 1; i <= n; i++){
    sum += i;
  }

  printf ("THE %dTH TRIANGULAR NUMBER IS %d\n", n, sum);

}

