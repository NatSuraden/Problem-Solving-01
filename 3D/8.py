import timeit
def reverse_slicing(s):
    return s[::-1]

def slicing_time():
    SETUP_CODE = ''' 
from __main__ import reverse_slicing 
'''
    TEST_CODE = ''' 
input_str = 'INE-KMUTNB'
reverse_slicing(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=5,number=100000)
    #print(times)
    print('Slicing time: {} '.format(min(times)))

if __name__ == "__main__":
    slicing_time()


def reverse_for_loop(s):
    sl = " "
    for c in s:
        sl = c + sl
    return sl

def For_loop_time():
    SETUP_CODE = ''' 
from __main__ import reverse_for_loop
'''
    TEST_CODE = ''' 
input_str = 'INE-KMUTNB'
reverse_for_loop(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=5,number=100000)
    #print(times)
    print('For_loop_time: {} '.format(min(times)))

if __name__ == "__main__":
    For_loop_time()

def reverse_while_loob(s):
    sl = " "
    length = len(s)-1
    while length >= 0:
        sl = sl+s[length]
        length = length-1
    return sl

def while_loob_time():
    SETUP_CODE = ''' 
from __main__ import reverse_while_loob
'''
    TEST_CODE = ''' 
input_str = 'INE-KMUTNB'
reverse_while_loob(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=5,number=100000)
    #print(times)
    print('while_loob_time: {} '.format(min(times)))

if __name__ == "__main__":
    while_loob_time()

def reverse_str_join(s):
    sl = "".join(reversed(s))
    return sl
def str_join_time():
    SETUP_CODE = ''' 
from __main__ import reverse_str_join
'''
    TEST_CODE = ''' 
input_str = 'INE-KMUTNB'
reverse_str_join(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=5,number=100000)
    #print(times)
    print('str_join_time: {} '.format(min(times)))
if __name__ == "__main__":
    str_join_time()

def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:])+s[0]

def reverse_recursion_time():
    SETUP_CODE = ''' 
from __main__ import reverse_recursion
'''
    TEST_CODE = ''' 
input_str = 'INE-KMUTNB'
reverse_recursion(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=5,number=100000)
    #print(times)
    print('reverse_recursion_time: {} '.format(min(times)))

if __name__ == "__main__":
    reverse_recursion_time()

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return "".join(temp_list)


def reverse_list_time():
    SETUP_CODE = ''' 
from __main__ import reverse_list
'''
    TEST_CODE = ''' 
input_str = 'INE-KMUTNB'
reverse_list(input_str)
'''

    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=5,number=100000)
    #print(times)
    print('reverse_listt_ime: {} '.format(min(times)))

if __name__ == "__main__":
    reverse_list_time()