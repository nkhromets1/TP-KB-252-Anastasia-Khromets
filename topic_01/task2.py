def test_string(text):
    print("Initial line:", text)
    print("strip():", text.strip())
    print("capitalize():", text.capitalize())
    print("title():", text.title())
    print("upper():", text.upper())
    print("lower():", text.lower())
text = input("Enter a string: ")
test_string(text)
