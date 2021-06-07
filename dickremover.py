shashamga = input('Dick? :')
split1 = shashamga.split(' ')
split1.remove('dick')
length = len(split1)


def function1(a, string1):
    while a < length:
        string1 += split1[a]
        a += 1
    print(string1)


function1(0, '')
