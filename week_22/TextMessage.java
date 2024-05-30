public class TextMessage extends Message {
    private String text;

    public String getText() {
        return text;
    }

    public void setText(String text) {
        if (text == null) {
            throw new IllegalArgumentException("Text cannot be null");
        }
        this.text = text;
    }

    @Override
    public int getSize() {
        return text.length();
    }
}
