# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        try:
            data = list(input().split(' '))
            for number in data:
                if len(number) > 0:
                    yield(number)   
        except (EOFError):
            return

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


t = get_number()

for i in range(0, t):
    a = get_number()
    b = get_number()
    a_bin = "{0:b}".format(a)
    b_bin = "{0:b}".format(b)
    
    a_same = a >> max(0,len(a_bin)-len(b_bin))
    b_same = b >> max(0,len(b_bin)-len(a_bin))
    a_bin_same = "{0:b}".format(a_same)
    b_bin_same = "{0:b}".format(b_same)
    
    precision_mask = (2**len(a_bin_same))-1
    mask = "{0:b}".format((~(a_same ^ b_same)) & precision_mask)
    
    try:
        common_from_msb = a_bin_same[0:mask.index('0')]
    except ValueError:
        common_from_msb = a_bin_same[0:]
    
    '''
    #print (a_bin)
    #print (b_bin)
    
    common_from_msb = ""
    for i in range(0, len(a_bin)):
        if i < len(b_bin) and a_bin[i] == b_bin[i]:
            common_from_msb += a_bin[i]
        else:
            break
    '''
    
    a_dist = len(a_bin) - len(common_from_msb)
    b_dist = len(b_bin) - len(common_from_msb)
    
    total_dist = a_dist + b_dist
    print (total_dist)