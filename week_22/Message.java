public abstract class Message {
    private String recipient;

    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        if (recipient == null || recipient.isEmpty()) {
            throw new IllegalArgumentException("Recipient cannot be null or empty");
        }
        this.recipient = recipient;
    }

    public abstract int getSize();
}
