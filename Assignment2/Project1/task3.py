
# HW Hints

# Task 3


def reverse(word):
    return word[::-1]


def is_palindrome(word):
    reversed_word = reverse(word)
    if reversed_word == word:
        return True
    else:
        return False


if __name__ == '__main__':

    # Ask the user to input a word
    word_input = input("Please enter a word to check if it is a palindrome: ")
    value = is_palindrome(word_input)

    print(word_input + " is a palindrome!") if value else print(word_input + " is not a palindrome!")
