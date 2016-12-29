def compl2(num):
    # negative_binary = ''
    # positive_binary = bin(int(num)[2:]
    # print 'positive binary: {}'.format(positive_binary)
    # for i, e in enumerate(positive_binary):
    #     digit = int(e)
    #     if digit == 0:
    #         total += 1*2**i
    # print total

    negative_binary = ''
    n = int(num)
    while n > 0:
        negative_binary = ('1' if n % 2 == 0 else '0') + negative_binary
        n /= 2
    print negative_binary
    negative_binary = bin(int(negative_binary, 2) + 1)
    print negative_binary

compl2(raw_input('number: '))