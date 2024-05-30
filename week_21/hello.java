```
Create a file called HelloWorld.java and add the following content:
 
  public class HelloWorld {
    public static void main(String[] args) {
      System.out.println("Hello, World");
    }
  }

Note: Java is very strict about file naming. Each file may only contain one (top-level) class and the
filename has to exactly match the name of that class.
Compile this program with javac HelloWorld.java. This creates a file HelloWorld.class – check that
is there with, e.g., ls. Now, run the file using java HelloWorld (without trailing .class). This should
print Hello, World! on the console.
See what happens if you rename HelloWorld.java to helloworld.java – try to compile it with javac
again. Remember how this error looks like so you can recognize it later on.
Bonus: You can view the bytecode with javap -c HelloWorld.
```

public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, World");
  }
}
