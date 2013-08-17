def squartRoot( guess, number):
    if good_enought(guess, number):
        return guess
    else:
        return squartRoot( nextGuess( guess, number), number)

def good_enought(guess, number):
    if abs( guess*guess - number) < 0.0001:
        return True
    else:
        return False

def nextGuess( guess, number):
    return ( guess + (number / guess)) / 2

if __name__=="__main__":
    firstGuess = 1.0
    number = raw_input("please enter the number:")
    squart_Root = squartRoot(firstGuess, float(number))
    print squart_Root
