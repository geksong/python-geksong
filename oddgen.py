from random import randint

def odd(n):
    return n%2;

allNums = []
for eachNum in range(9):
    print eachNum
    allNums.append(randint(1,99))

if __name__ == '__main__':
    print allNums
    print filter(odd, allNums)
