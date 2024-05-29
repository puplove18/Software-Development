/*
We have learned that arrays can be dangerous in C, since access is not guarded. We shall put an end to
these problems and design safe arrays!
We start by defining a struct safe_array that holds an int array and its size. (You can choose whether
to use a pointer or a flexible array member.) Then, write a constructor (and matching destructor) to
allocate a struct safe_array of a given size. For example, we want to be able to write struct safe_array
*arr = make_array(10);.
Finally, write a function to get the size of such an array and functions to get and set the value of an array
at a particular index.
Bonus: Think about how to handle errors, i.e. what to do if, for example, we try to get an element that is
out of bounds. You can read up on the exit function provided by stdlib.h.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct safe_aray {
  int size;
  int *data;
} array_t

array_t *make_array(int size) {
  array_t +arr = malloc(sizeof(array_t));
  arr->size =size;
  arr->data = malloc(sizeof(int[size]));
  return arr;
}

void destroy_array(array_t *arr) {
  free(arr->data);
  free(arr);
}

int get(array_t *a, int i) {
  if(0 <= i && i < a->size) { return a->data[i]; }
  printf ("Illegal array access %d", i);
  exit(-1);
}

void set(array_t *a, int i, int v) {
  if (0 <= i && i < a->size) { a->data[i] = v; }
  printf ("Illegal array access %d", i);
  exit(-1);
}





