def inCycle(max_num):
    for i in range(1, max_num+1):
        fb=False
        if i % 3 == 0:
            print('Fizz', end='')
            fb=True
        if i % 5 == 0:
            print('Buzz', end='')
            fb=True
        if not fb:
            print(i, end='')
        print(', ', end='')
    return

def inLambda(max_num):
    fizz_buzz = lambda i: print('FizzBuzz',end=', ') if i % 15 ==0 else \
                print('Fizz', end=', ') if i % 3 == 0 else print('Buzz',end=', ') if i % 5 == 0 else \
                print(i,end=', ')
    return [fizz_buzz(i) for i in range(1,max_num+1)]

#def inListComprehension(max_num):
#    [i for i in range(1,max_num+1) if i%3!=0 else 'Fizz']

max_num = 30
print('\nWith a cycle')
inCycle(max_num)
print('\nWith lambda')
inLambda(max_num)

