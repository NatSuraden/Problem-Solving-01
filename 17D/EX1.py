import timeit
list1 = [1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
def Sequential(list1):
    index = -1
    for i in list1:
        index  +=1
        if i == 37:
            return index
def Seq_time():
    SETUP_CODE='''
from __main__ import Sequential
'''
    TEST_CODE = '''
list1 = [1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
Sequential(list1)
'''
    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=5,number=10000)
    print('times:{}'.format(min(times)))

if __name__=="__main__":
    Seq_time()