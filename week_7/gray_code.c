/*
Produce a Gray code for given n variables. Concretely, your program should ask a user for the number n
and then the names of the variables. Then, your program should output a Gray code for these variables,
i.e. a sequence of binary strings such that between each only one bit changes.
You may use the following idea to generate Gray codes:
• A Gray code for one variable is 0 and 1
• A Gray code for n variables can be obtained as follows:
– Take a Gray code for n ≠ 1 variables (call it L)
– Copy L to a new list M and reverse M
– Append a 0 to all codes in L, append a 1 to all codes in M
– Concatenate L and M
Hint: Break down the task into smaller bits:
• How to copy a sequence of codes
• How to reverse a sequence (or copy it in reverse)
• How to append something to every element of a sequence
• How to concatenate two sequences
One example output for input 3:

000
100
110
010
011
111
101
001
(Note: Gray codes are not unique, so there are multiple correct solutions!)
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int n;
  printf("How many variables? ");
  scanf("%d", &n);

  int size = 2;
  char **code = malloc(sizeof(char *[size]));
  codes[0] = malloc(sizeof(char[n]));
  codes[0][0] = '0';
  codes[1] = malloc(sizeof(char[n]));
  codes[1][0] = '1';

  for (int i = 1; i < n; i++) {
    codes = realloc(codes, sizeof(char *[size * 2]));
    for (int j = 0; j < size; j++) {
      codes[size + j] = malloc(sizeof(char[n]));
      memcpy(codes[size + j], codes[size - j - 1], n);
    }
    for (int j = 0; j < size; j++) {
      codes[j][i] = '0';
      codes[size + j][i] = '1';
    }
    size *= 2;
  }

  for (int i = 0; i < size; i++) {
    for (int j = 0; j < n; j++) {
      putchar(codes[i][j]);
    }
    putchar('\n');
  }
}
  












  scanf("%d", &n);
