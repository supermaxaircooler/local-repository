while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        print(int(reply)** 2)
    except ValueError:
        print("bad input")
        
print('Bye')