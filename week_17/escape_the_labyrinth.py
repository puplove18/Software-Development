```
Our goal is to implement a game where the player has to escape a labyrinth. First, we need a way to
define “levels”. A labyrinth is given by a text file, where X means wall, _ is open space, S is the starting
position, E is an exit, and G is gold that the player can collect. For example, a level could look like this:
   XEX______G
   X_X_X_XXXX
   X___X__S__
Write code to read in the level from level.txt. Check that the input is well formed, e.g. there is exactly
one S, at least one E, etc. Store the level in an appropriate object and, for testing, print the level you loaded.
Next, define an object to represent the player. The player has the position where they are currently, how
many steps they have taken, how much gold they have collected, etc.
Now, we need to implement displaying of what the user sees. For this, we use the Python package curses.
This package allows to draw very complicated textual interfaces. We will only use basic features without going into detail.
Start from the following code:

  from curses import wrapper
  
  def main(stdscr):
    x, y = 0, 0
    while True:
      # Clear screen
      stdscr.clear()
      # Print "Hello" at coordinate y, x; y first for historical reasons
      stdscr.addstr(y, x, "Hello")
      # Actually write out the data to the terminal
      stdscr.refresh()
      # Wait for a key to be pressed
      c = stdscr.getkey()
      if c == "KEY_DOWN":
        y += 1
      elif c == "KEY_UP":
        y -= 1
      elif c == "KEY_RIGHT":
        x += 1
      elif c == "KEY_LEFT":
        x -= 1
  if __name__ == "__main__":
    wrapper(main)
  
With this code, you can move the text Hello around on the screen.
Modify the code so that the player can run around in the labyrinth. Indicate their position with a P.
(curses also supports blinking, coloured, ... text.)
Track gold that the player picks up and print the score if the player reaches the exit (e.g. the score could be gold Æ100 ≠steps).
To make the game a bit more interesting, reduce the “vision” of the player and only display the immediate surroundings.
```
