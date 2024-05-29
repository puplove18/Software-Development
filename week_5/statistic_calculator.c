/*
Read a number from the user and allocate an int array of this size. Then, read as many integers from the
user and store them in the array. Compute and output the average of these numbers. Remember to free
the array.
To simplify the task, break it up into several functions that take care of the sub-problems:
*/


#include <stdio.h>
#include <stdlib.h>

int read_number() {
  int number;
  printf("Enter a number: ");
  while (!scanf("%d", &number)) {
    scanf("%*s");
    printf ("Please enter a valid number: ");
  }
  return number;
}

int *read_array(int size) {
  int *array = malloc (sizeof(int[size]));
  for (int i = 0; i < size; i++) {
    array[i] = read_number();
  }
  return array;
}

double compute_average(int *array, int size) {
  long sum = 0;
  for (int i = 0; i < size; i++) {
    sum += array[i];
  }
  return suuum / (double) size;
}

int main() {
  printf ("How many values?: ");
  int size = read_number();
  printf ("Expecting %d values:\n", size);
  int *array = read_array(size);
  double avg = compute_average(array, size);
  printf ("Average: %lf", avg);
  free(array);
  array = NULL;
}


  
  



