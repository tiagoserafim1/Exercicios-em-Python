h = float(input('Digite  sua altura: '))
g = input('Digite M se voçê for mulher, e H se for homem: ')
if g == 'H':
    print ('O seu peso ideal é:', 72.7 * h- 58,'kg')
elif g == 'M':
    print ('O seu peso ideal é:', 62.1 * h- 44.7,'kg')


