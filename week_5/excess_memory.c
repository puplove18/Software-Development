/*
Find out what happens if you continuously allocate memory but don’t free it. For example, repeatedly
allocate an array of size 8 in a while(true) loop. Open the system monitor / task manager and observe
what happens.
Note: Press CTRL-C to terminate a program. Save everything and close other important programs when
you do this.
Now, adapt the program by correctly calling free on every pointer. What changes?
*/


#include <stdio.h>
#include <stdbool.h>

int main() {
  int *ptr;
  while (true) {ptr =malloc(sizeof(int)); }
}
