/*
Implement the function int strcpy2(char dst[], char src[]) that copies a given C-string src into dst
and returns the number of characters written. Do not use any functions of string.h!
Test your implementation
*/

#include <stdbool.h>

int strcpy2(char dst[], char src[]) {
  int i = 0;
  char chr;
  while (true) {
    chr =src[i];
    dst[i] = chr;
    i++;

    if (chr == 00) return i;
  }
}
