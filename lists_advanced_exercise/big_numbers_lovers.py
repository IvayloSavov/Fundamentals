input_list = input().split()

input_list.sort(reverse=True)
# input_list.reverse() за обратния ред може да се ползва и това
print("".join(input_list))