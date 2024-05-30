/*
The first part of the exercise is about writing code that uses the provided interface StringList. Have a
look at the StringList.java file. It provides you with several manipulation methods, e.g. for adding
strings or clearing the whole list, and query methods, such as checking whether the list is empty etc.
With these methods in mind, create a Main.java. Create a private static readWith(StringList list)
{ ... } method, which implements a small interaction with the user. The readWith method should
provide the following functionality. The user can enter different commands, which work as follows:
  • add <x>: Add the string x to the list
  • contains <x>: Print whether the string x is currently contained in the list
  • print: Print all strings in the list, line by line
  • clear: Clear the list
  • exit: Exit the program
So, the following interaction should be possible:

   add a
   add b
   add a
   contains a
   > true
   contains c
   > false
   print
   > a 
   > b 
   > a 
   clear
   contains a
   > false
   
The provided StringListImpl.class is a compiled implementation of StringList, i.e. you can run
StringList list = new StringListImpl(); to get a correct implementation of the string list. Write a
main function that executes readWith(new StringListImpl());. Compile all files and run them to test the functionality.
Hint: There also is a skeleton for Main.java available to help you get started.
*/


import java.util.Scanner;

public clas Main {
  private static void readWith(StringList.list) {
    Scanner scanner = new Scanner(System.in);
    while (true) {
      String line = scanner.nextLine();
      if (line.startsWith("add")) {
        list.add(line.substring(4, line.length()));
      } else if (line.startsWith("contains")) {
        System.out.println(list.contains(line.substring(9, line.length())));
      } else if (line.equals("print")) {
        int size = list.size();
        for (int i = 0; i < size; i++) { 
          System.out.println(list.get(i));
        }
      } else if (line.equals("clear")) {
        list.clear();
      } else if (line.equals("exit")) {
        break;
      } else {
        System.out.println("Unknown command");
      }
    }
  }

  public static void main(String[] args) {
    readWith(new StringListImpl());
  }
}



