/*
Create a MyStringList.java file, define public class MyStringList implements StringList, and imple-ment the required methods.
Hint: Use an array list approach (similar to a previous C exercise). Declare members private String[]
array; and private int pos;. The array initially has size 4, and pos indicates the next free position in
the array. After adding 4 elements, we would have pos == array.length. When we want to add another
element, we need to create a larger array – create one with size 2 * array.length and copy over all the
old elements. (Note the importance of declaring array and pos as private, if outside code would mess with it, this list would not work correctly.)
After implementing your variant of the StringList, replace the usage of StringListImpl in your Main with MyStringList and check that it still works.
Hint: There is a skeleton for MyStringList.java available to help you get started.
*/


import java.util.Arrays;
import java.util.Objects;

public class MyStringList implements StringList {
  private String[] array;
  private int pos;

  public MyStringList() {
    array = new String[4];
    pos = 0;
  }

  @Override
  public boolean isEmpty() {
    return pos == 0;
  }

  @Override
  public int size() {
    return pos;
  }

  @Override
  public boolean contains(String string) {
    for (int i = 0; i < pos; i++) {
      if (Objects.equals(array[i], string)) {
        return true;
      }
    }
    return false;
  }
  @Override
  public void add(String string) {
    if (pos == array.length) {
      array = Arrays.copyOf(array, array.length * 2);
    }
    array[pos] = string;
    pos += 1;
  }

  @Override
  public void clear() {
    pos = 0;
  }
}
  


