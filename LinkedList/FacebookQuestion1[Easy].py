
num = 11110000111100001111000011110000
# return 0000 1111 000011110000111100001111
#
s = ""
while num > 0:
    r = num %10
    s +=str(r)
    num = num//10

print(s)