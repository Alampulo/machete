# def palin(n):
#     return n == n[::-1]
#

    '''
    [mom, letter, racecar]
    '''



'''
second solution
'''

def palindrome():
    a = ['mom', 'letter', 'bob']

    pal = []

    for word in a:

        if word == word[::-1]:

            pal.append(word)
    print(pal)

palindrome()
