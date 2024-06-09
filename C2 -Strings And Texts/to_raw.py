string = r"I love the\tsense of    fear.\nAre you afraid"

def to_raw(string):
    return fr"{string}"
print(to_raw(string))