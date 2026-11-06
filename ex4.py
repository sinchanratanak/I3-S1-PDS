# (b) safe converter
def safe_int(text):
    """Turn text into an int; return None when it is not a number."""
    text = text.strip()
    if text.lstrip("-").isdigit():         # "42" or "-42",isdigit is function that return only T or F
        return int(text)
    try:
        return int(float(text))            # "3.9" -> 3
    except ValueError:
        return None                        # "abc", "", "12a"


for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample)) #repr: is function that provide the original value

#(c) sum
a = safe_int(input("First number: "))
b = safe_int(input("Second number: "))
if a is None or b is None:
    print("Error, please enter valid numbers!")
else:
    print(f"Sum:{a+b}")