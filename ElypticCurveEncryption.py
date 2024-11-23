#Get Mod, added for readability
def mod(x, m):
    return x % m

#Get Inverse, added for readability
def inv(x, m):
    return pow(x, -1, m)

#Point double, used to calculate 2P
def twoP(x1, y1, a, m):
    numerator = mod(3 * (x1 ** 2) + a, m)
    denominator = mod(2 * y1, m)
    lambda1 = mod(numerator * inv(denominator, m), m)
    x2 = mod(lambda1 ** 2 - 2 * x1, m)
    y2 = mod(lambda1 * (x1 - x2) - y1, m)
    return x2, y2

#Point Addition, Add P to iP
def PAddOne(x1, y1, x2, y2, a, m):
    denominator = mod(x2 - x1, m)
    if denominator == 0:
        if (y2 != y1):
            print("Hit Infinity/Identity Point")
        return twoP(x1, y1, a, m)
    numerator = mod(y2 - y1, m)
    lambda2 = mod(numerator * inv(denominator, m), m)
    x3 = mod(lambda2 ** 2 - x1 - x2, m)
    y3 = mod(lambda2 * (x1 - x3) - y1, m)
    return x3, y3


if __name__ == '__main__':
    m = 23
    a = 1
    P = (3, 10)

    points = []
    pseen = set()

    curr_point = P
    points.append(curr_point)
    pseen.add(curr_point)

    i = 2
    while curr_point != P or i == 2:
        next_x, next_y = PAddOne(P[0], P[1], curr_point[0], curr_point[1],a, m)
        if (next_x, next_y) in pseen:
            break
        points.append((next_x, next_y))
        pseen.add((next_x, next_y))
        curr_point = (next_x, next_y)
        i += 1

    print(f"Points in the group E(Z23) generated from P = (3, 10):")
    for i, point in enumerate(points, 1):
        print(f"{i}P: {point}")