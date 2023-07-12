

# d = {"a": 1, "b":2, "c":3}
# for i in d.keys():
#     print(i)

# our_list = ["alpha", "beta", "gamma"]


# for i in range(len(our_list)):
#     print(our_list[i])

# better
# for element in our_list:
#     print(element)

# not better
# for i in range(len(our_list)):
#     print(f"{i} --> {our_list[i]}")

# better
# for index,val in enumerate(our_list):
#     print(f"{index} --> {val}")

# list comprehensions / dict comprehensions




our_dict = {"alpha":1, "beta":2, "gamma":3}

# for key in our_dict.keys():
#     print(key)

# for key in our_dict:
#     print(key)

# for (key,val) in our_dict.items():
#     print(f"key is {key}, value is {val}")

our_list = ["alpha", "beta", "gamma", "alpha", "alpha", "beta"]

# counting
count_dict = dict()
for element in our_list:
    # if its already in our_dict
    if element in count_dict.keys():
        count_dict[element] += 1
    else:
        count_dict[element] = 1

count_dict = dict()
for element in our_list:
    # if its already in our_dict
    count_dict[element] = count_dict.get(element, 0) + 1

# from collections import counter

print(count_dict)

