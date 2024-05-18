ciphertext = 'afZ_r9VYfScOeO_UL^RWUc'
#a 97 f 102 Z 90 _ 95    r 114
#f 102 l 108 a 97 g 103   { 123
#+5     +6     +7    +8   +9


j = 5
for i in ciphertext:
    print(chr(ord(i) + j), end='')
    j += 1

