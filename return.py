def square(x):
    print('--start--')
    return x * x 
    print('--end--') # Dead Code

print(square((3)))
print('hola!')


"""
return 문의 역할은 
함수를 즉시 종료하면서 값을 돌려준다.

"""


mystring = 'were you stung?'
mystring += ' Yes, but it was just a bee'
print(mystring)

for lett in mystring:
    lett += 'with flowers \n\n'
print(lett) 