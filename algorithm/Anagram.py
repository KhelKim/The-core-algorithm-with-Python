string1 = "AF"
string2 = "ASDFASDFASDFDJAJSDJFJASDKFJASDF"


def get_dict(string):
    str_list = list(string)
    str_set = list(set(str_list))
    dictionary = {}
    for alpha in str_set:
        dictionary[alpha] = str_list.count(alpha)
    return dictionary


check_dic = get_dict(string1)
count = 0
for i in range(len(string2)):
    dic = get_dict(string2[i:i + len(string1)])
    if check_dic == dic:
        count += 1
print(count)