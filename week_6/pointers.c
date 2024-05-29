/*
Define a struct that can store a 2D-point, i.e. an x- and y-coordinate. Write a function that takes a point
and prints it to the console.
Also write a function that reads coordinates from the user and stores them in a point. (Remember to use
a constructor or initializer.)
Bonus: Create a set of basic point functions to work with points. For example: Adding two points
together, compute the (euclidean) distance of two points, multiply with a given scalar, …
*/


#include <stdio.h>
#include <stdlib.h>

typedef struct point {
  int x;
  int y;
} point_t;

void print_point(point_t *p) {
  printf ("(%d, %d)", p->s, p->y);
}

point_t *create_point(int x, int y) {
  point_t *p = malloc(sizeof(point_t));
  p->x = x;
  p->y = y;
  return p;
}

point_t *read_point() {
  int x, y;
  printf ("Enter two coordinates: ");
  scanf ("%d, %d", &x, &y);
  return create_point(x, y);
}
