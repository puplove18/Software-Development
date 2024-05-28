/*
Ask the user for a number between 0 and 100. Then, read this many numbers from the user. Finally,
compute the average of these numbers.
Example:
1 How many numbers? 6
2 Please enter your 6 numbers: 1 2 9 8 -2 3
3 Avg: 3.500, Var: 14.917
*/

#include <stdio.h>
#include <math.h>

int main() {
  double numbers[100], number;
  int count;
  printf("How many numbers? ");
  scanf(%d", &count);
  printf("Please enter your %d numbers", count);
  for (int i  = 0; i < count; i++) {
    scanf("%lf", &number);
    numbers[i] = number;
  }

  double sum = 0.0;
  for (int i = 0; i < count; i++) {
    sum += numbers[i];
  }
  
  double average = sum / (double) count;
  double sum_of_squares = 0.0;
  for (int i = 0; i < count; i++) {
    double value = numbers[i] - average;
    sum_of_squares += value * value;
  }

  double variance = sum_of_squares / count;
  printf("Avg: %.3lf, Var: %.3lf\n", average, variance);
}

