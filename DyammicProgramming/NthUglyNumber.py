

# def nthUglyNumber(n):
#
#     s = {1}
#     print(type(s))
#     mi = 1
#     # lst = list()
#     for i in range(1,n+1):
#         s.add(i*2)
#         s.add(i*3)
#         s.add(i*5)
#         print(s)
#         mi = min(s)
#         s.remove(mi)
#         print("Printing minimum " ,mi)
#         if i == n :
#             return mi
#
#     return mi


# def nthUglyNumber(n):
      # " This is a solution which takes n as input and  solves the problem in order(n) time and space "
#     mi = 1
#     s = {1}
#     for i in range(1,n+1):
#         mi = min(s)
#         # s.add(mi *2)
#         # s.add(mi *3)
#         # s.add(mi *5)
#         # s.union({mi * 2,mi *3,mi *5})
#         s = s.union({mi * 2,mi *3,mi *5})
#         # print(s)
#         s.remove(mi)
#         print(i , "th ugly number is " , mi)
#
#         if i == n:
#             return mi
#
#

# def nthUglyNumber(n):
#     """
#     This is a method to find ugly number using dynammic programming approach
#     """
#     un = [] * n
#
#     p2 = p3 = p5 = 0
#     un.insert(0,1)
#     for j in range(1,n):
#
#         mi = min(un[p2] * 2,
#                  un[p3] * 3,
#                  un[p5] * 5)
#         un.insert(j,mi)
#
#         if mi == un[p2] * 2:
#             p2 +=1
#         if mi == un[p3] * 3:
#             p3 +=1
#         if mi == un[p5] * 5:
#             p5 +=1
#
#     return un[n-1]


# another simple approach

def isugly(n):
    if n%2==0 or n%3==0 or n%5==0:
        return True
    return False

def nthUglyNumber(n):
    count = 1
    num = 2;
    number = 0
    i=1
    while(count < n):
        i+=1
        if isugly(i) == True:
            count +=1
    return i


if __name__=="__main__":
    n = 10
    print("Printing",n,"th  Ugly Number " , nthUglyNumber(n))