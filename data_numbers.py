def readInt(msg = ''):

    while True:

        try:
            x = str(input(msg)).strip()
            x = int(x)
        
        except:

            print(f'{x} is not a valid integer. Try again!')
            continue

        else:
            return x
