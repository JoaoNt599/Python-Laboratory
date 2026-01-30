from heap import headpify, heappop, heappush


a_list = ['D', 'H', 'E', 'Y', 'L', 'C' ]
headpify(a_list)
print(a_list)


heappop(a_list)
print("After popping")
print(a_list)

############################################

t_list = ['L', 'A', 'T', 'C', 'D']
headpify(t_list)
while len(t_list) > 0:
    print(heappop(t_list))

############################################

o_list = ['F', 'D', 'G', 'S', 'T']
headpify(o_list)
heappush(o_list, "Z")
print(o_list)