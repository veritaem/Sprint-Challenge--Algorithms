'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# a note here: using a global variable failed the tests because it didnt reset between tests(!!)
# is there a way i could reset it between them?  Thanks!

def count_th(word):
    if len(word) == 0:
        print('too small!')
        return 0
    elif word[0:2] == 'th':
        print(f'{word[0:2]} contains th ')
        return 1 + count_th(word[1:])
    else:
        print(f'{word[0:2]} does NOT contain th')
        return count_th(word[1:])


    
    
print(count_th('THtHThth'))