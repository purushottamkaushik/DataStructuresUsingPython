

def MajorityElement ( A ):
    my_dict = {}

    for i in A:
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] +=1

    print(my_dict)

    majority_element = 0

    for key ,value in enumerate(my_dict):
        print(key , value)



MajorityElement([1,3,4,2,1,2,2,2,2])