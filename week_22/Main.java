/*
Create two files, one called Message.java and another called TextMessage.java. In each, create a
class with the appropriate name and let TextMessage extend Message. Add a private String recipient
member to Message as well as a matching getter and setter method, i.e. public String getRecipient()
and public void setRecipient(String name). Compile both files using javac to check if there are any syntax errors.
Create a third file Main.java with main() method. In this main method, create a TextMessage and call
setRecipient("user") on it. After this, print the result of getRecipient() using System.out.println().
Compile the Main.java as well and run it.
*/


public class Main {
    public static void main(String[] args) {
        TextMessage textMessage = new TextMessage();
        textMessage.setRecipient("user");
        textMessage.setText("Hello, this is a text message!");

        System.out.println("Recipient: " + textMessage.getRecipient());
    }
}
