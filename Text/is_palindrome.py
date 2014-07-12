while True:
    inputs = raw_input('input a string:')
    if inputs == 'exit':
        break
    elif inputs[::-1] ==inputs:
        print 'palindrome'
    else:
        print 'not palindrome'
    
