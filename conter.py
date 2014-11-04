def conter(count_sat=0):
    count = [count_sat]
    def incr():
        count[0] += 1
        return count[0]
    return incr

if __name__ == '__main__':
    timer = conter(8)
    print timer()
    print timer()
    print timer()
