public class Main {
    public static void main(String[] args) {
        TextMessage textMessage = new TextMessage();
        textMessage.setRecipient("user");
        textMessage.setText("Hello, this is a text message!");

        System.out.println("Recipient: " + textMessage.getRecipient());
    }
}
