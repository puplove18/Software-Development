/*
Implement a stack, as we have seen in the lecture. Start by defining a struct that stores a (dynamically
allocated) array, the size of the array, and the “fill level” of the array (just as with an array list). Define a
constructor and destructor as well as the following functions:
• size (get the size of the stack, i.e. how many elements are on it),
• push (add a new element “on top” of the stack), and
• pop (remove and return the topmost element) functions.
Now, add dynamic resizing functionality, i.e. whenever we push an element but the array is full (fill level
= size), move all the data to a new array twice the size.
We want to be able to use the list in the following way:


int main() {
  array_stack *s = make_stack();
  size(s); // Returns 0
  push(s, 1);
  push(s, 2);
  size(s); // Returns 2
  pop(s); // Returns 2
  while (true) {
    int data;
    scanf("%d", &data);
    push(s, data);
    if (data == 0) {
      break;
    }
  }
// Etc.
}

Test the functionality.
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct array_stack {
  int size;
  int top;
  int *data;
} stack_t;

stack_t *make_stack() {
  stack_t *stack = malloc(sizeof(stack_t));
  stack->size = 8;
  stack->data = malloc(sizeof(int[8]));
  stack->top = 0;
}
void destroy_stack(stack_t *stack) {
  free(stack->data);
  free(stack);
}

bool is_empty(stack_t *stack) {
  return stack->top == 0;
}
int size(stack_t *stack) {
  return stack->top;
}
void push(stack_t *stack, int element) {
  if (stack->top == stack->size) {
    stack->data = realloc(stack->data, sizeof(int[stack->size * 2]));
    stack->size *= 2;
  }
  stack->data[stack->top] = element;
  stack->top += 1;
}

int pop(stack_t *stack) {
  if (is_empty(stack)) {
    printf("Attempt to pop empty stack!\n");
    exit(1);
  }
  stack->top -= 1;
  return stack->data[stack->top];
}

int main() {
  stack_t *s = make_stack();
  size(s); // Returns 0
  push(s, 1);
  push(s, 4);
  size(s); // Returns 2
  pop(s); // Returns 2
  while (true) {
    int data;
    scanf("%d", &data);
    push(s, data);
    if (data == 0) {
      break;
    }
  }
}









#include <
