

x = 4

try:
    if x < 5:
        raise ValueError('X is less than 5')
    
except Exception as err:
    print('Error:', err)

else:
    print('No error occured')

finally:
    print('Runs with or without error')



    