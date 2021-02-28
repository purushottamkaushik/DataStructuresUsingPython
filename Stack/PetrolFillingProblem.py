petrol  = [1,2,3,4,5]
distance  = [3,4,5,1,2]
#  petrol filling problem.....

def tour(petrol,distance):

    start = 0
    sum = 0
    diff = 0

    for i in range(len(petrol)):
        sum = sum + petrol[i] - distance[i]

        if sum < 0 :
            start = i + 1
            diff +=sum
            sum = 0

    return start if start - diff >=0 else -1







print(tour(petrol,distance))


# Petrol
# def getTour(petrol, distance, n):
#     s, start, diff = 0, 0, 0
#     for i in range(n):
#         s = s + petrol[i] - distance[i]
#         if (s < 0):
#             start = i + 1
#             diff += s
#             s = 0
#     if s + diff > 0:
#         return start
#     else:
#         return -1
#
#
# if __name__ == '__main__':
#     petrol = [4, 6, 7, 4]
#     distance = [6, 5, 3, 5]
#     value = getTour(petrol, distance, 4)
#     print(value)



















# def tour(petrol,distance):
#     start = 0
#     sum = 0
#     diff = 0
#     for i in range(len(petrol)):
#         sum = sum + petrol[i] - distance[i]
#
#         if sum < 0:
#             start = i + 1
#             diff +=sum
#             sum = 0
#
#     return start if sum+diff>=0 else -1


#
# def tour(petrol, distance, n):
#     start = 0
#     end = 1
#     curr_petrol = petrol[start] - distance[start]
#     while end != start or curr_petrol < 0:
#         while curr_petrol < 0 and start != end:
#             curr_petrol = curr_petrol - (petrol[start] - distance[start])
#             start = (start + 1) % n
#             if start == 0:
#                 return -1
#         curr_petrol = curr_petrol + petrol[end] - distance[end]
#         end = (end + 1) % n
#     return start
#
#
# if __name__ == '__main__':
#     petrol = [4, 6, 7, 4]
#     distance = [6, 5, 3, 5]
#     value = tour(petrol, distance, 4)
#     print(value)