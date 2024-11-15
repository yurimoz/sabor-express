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
        

def readFloat(msg = ''):

    while True:

        try:
            x = str(input(msg)).strip()
            x = float(x)
        
        except:

            print(f'{x} is not a valid number. Try again!')
            continue

        else:
            return x


def validate_entry(msg = '', lowerlim = 1, upperlim = 10):

    while True:
        entry = readInt(msg)
        if lowerlim <= entry <= upperlim:
            break
        else:
            print(f'{entry} is not a valid option')
    
    return entry