```
Create a simple calculator that reads an inline expression such as 5 + 10. The calculator should support
the four basic mathematical operations. First, just assume that the user provides in put in the correct
format, i.e. a number, an operation symbol, and another number, and display the result.
Next, add error handling. Concretely, if the user enters something that does not match the format, print an error.
Finally, let the calculator run in a loop.
Bonus: Make the calculator interactive and allow the use of ans (the previous result). For example, when
entering 5 + 5 and ans * 2, the calculator should print 10 and 20.
Also implement referring to previous results with Mn, where nis a number, and Mnrefers to the result
from nsteps ago (this means that M1 is ans). Example: 5 + 5, ans * 2, ans - M2 should print 10 as final result.
```

import java.util.InputMismatchException;
import java.util.Scanner;

public class Calculator {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    while (true) {
      try {
        system.out.print("Please ennter: ");
        double first = scanner.nextDouble();
        String operation = scanner.next();
        double second = scanner.nextDouble();

        if (operation.equals("+")) {
          System.out.println(first + second);
        } else if (operation.equals("-")) {
          System.out.println(first - second);
        } else if (operation.equals("*")) {
          System.out.println(first * second);
        } else if (operation.equals("/")) {
          if (second == 0.0) {
            System.out.println("Division by zero!");
          } else {
            System.out.println(first / second);
          }
        } 
      } catch (InputMismatchException e) {
        scanner.nextLine();
        System.out.println("Illegal input!");
      }
    }
  }
}





