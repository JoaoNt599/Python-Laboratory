from heap import heappush, heappop, headpify


def find_min_const(ropes):
    headpify(ropes)
    cost = 0
    while len(ropes) > 1:
        sum = heappop(ropes) + heappop(ropes)
        heappush(ropes, sum)
        cost += sum
    return cost