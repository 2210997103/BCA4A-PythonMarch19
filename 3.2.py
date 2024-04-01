print("name ishika roll no 2210997103")
def is_pos_neg_or_zero(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
num = float(input("Enter a number: "))
print("The number is", is_pos_neg_or_zero(num))
