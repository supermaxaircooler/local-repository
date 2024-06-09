try:
    print("in try statement")
    raise IndexError
except IndexError:
    print("in except statement")
    raise IndexError
except IndexError:
    print("in second index error statemnt")
finally:
    print("in finally statement")