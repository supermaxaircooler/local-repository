def fn():
    while True:
        reply = input('Enter text:')
        if reply == 'stop': break
        elif not reply.isdecimal():
            print("bad input")
        else:
            print(float(reply) ** 2)
    return 0

if __name__ == "__main__":
    fn()
