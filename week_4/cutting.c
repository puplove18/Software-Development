/*
Write a function strins that takes two strings s, t and an integer pos. This function should insert the
string t at position pos into s. You can assume that s is large enough to fit t. Test your function. For
example, given "Hello!", ", World" and 5, your function should modify s to contain "Hello, World!".
Hint: Use strlen from string.h to determine the size of a given string.
Bonus: Make the function interactively usable. Allocate a large char array s and repeatedly read a
position and string to insert into s until the user wants to exit.
Extra bonus: Add further editing operations, e.g. deleting a range, or copy and paste.
*/

#include <stdio.h>
#include <string.h>

void strings(char *s, char *t, int pos) {
  size_t len_s = strlen(s);
  size_t len_t = strlen(t);
  if (len_s <= pos) {
    strcat(s, t);
    return;
  }
  for (int i = len_s; i >= pos; i--) { s[i + len_t] = s[i]; }
  for (int i = 0; i < len_t; i++) { s[pos + i] = t[i]; }
}

int main() {
  char s[1024] = "HELLO!";
  char t[] = ", WORLD";
  strings (s, t, 5);
  printf("%s", s);
}
