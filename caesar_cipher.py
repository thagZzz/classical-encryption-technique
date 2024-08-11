def caesar_cipher(text, shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # If it's not an alphabetic character, just add it
        else:
            result += char

    return result

# Example usage
text = "Hello, World!"
shift = 3
print(f"Original Text: {text}")
print(f"Encrypted Text: {caesar_cipher(text, shift)}")

