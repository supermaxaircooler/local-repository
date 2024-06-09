try:
    raise IndexError('spam') from ValueError # Exceptions remember arguments
except IndexError as clause:
    print('propagating')
    print(clause.__cause__)

print(" how are ya????")
raise KeyError("lode ki sarkar")
