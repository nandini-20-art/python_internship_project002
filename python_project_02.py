def count_words(text):
    """
    This function counts the number of words in a given text.

    Args:
      text: The string of text to count words from.

    Returns:
      The number of words in the text, or 0 if the text is empty.
    """
    # Remove leading and trailing spaces
    text = text.strip()

    # Handle empty input
    if not text:
        return 0  # No words in empty text

    # Split the text into words using spaces as delimiters
    words = text.split()

    # Return the number of words
    return len(words)


# Get input from the user
user_text = input("Enter a sentence or paragraph: ")

# Count the words
word_count = count_words(user_text)

# Display the result
print("Word count:", word_count)