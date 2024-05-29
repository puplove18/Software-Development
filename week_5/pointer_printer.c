/*
Write a function that prints the contents of a given dynamically allocated int array. Your code should
look like this:


void print_int_array(int *array, int size) {
// TODO
}
int main() {
  int *array = malloc(sizeof(int[5]));
  for (int i = 0; i < 5; i++) {
    array[i] = i;
  }
  print_array(array, 5);
  free(array);
}

Modify the part the fills the array to verify that your function works.
*/


#include <stdio.h>
void_print_array(int *array, int size) {
  for (int i = 0; i < size; i++) {
    printf("%d", test[i]);
  }
  printf("\n");
}
