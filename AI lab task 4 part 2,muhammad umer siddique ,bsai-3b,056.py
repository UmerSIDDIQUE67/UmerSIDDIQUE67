def remove_punctuation(input_string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for char in input_string:
        if char not in punctuation:
            result += char
    return result
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    cleaned_string = remove_punctuation(user_input)
    print(f"String without punctuation: {cleaned_string}")



