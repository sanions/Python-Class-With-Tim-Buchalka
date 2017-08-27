
with open('L64/sample.txt', 'a') as poem:
    poem.write('\r\n')
    for i in range(2, 13):
        for j in range(1, 13):
            poem.write('{0} times {1} is {2}\r\n'.format(i, j, i*j))
        poem.write('-------------------\r\n')
