def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#(a)
for s in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
    print(f"{s:>5} -> {letter_grade(s)}")

#(b)  test for A+ come before the test for A becuase an "elif" stops at the first condition. A score like 99 is both >= 97 and >=90, so if >= 90 come first, it return "A" and the "A+" never run.