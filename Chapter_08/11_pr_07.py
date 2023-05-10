def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Aerish is a good boy    "
n = remove_and_split(this, "Aerish")
print(n)
# int(this.strip()p)r