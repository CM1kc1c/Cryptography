solutions = []

for x1 in [0, 1]:
    for x2 in [0, 1]:
        for x3 in [0, 1]:
            for x4 in [0, 1]:
                for x5 in [0, 1]:
                    for x6 in [0, 1]:
                        for x7 in [0, 1]:
                            if (x1 + x2 + x3 + x4) % 2 == 0 and \
                               (x2 + x3 + x4 + x5) % 2 == 1 and \
                               (x3 + x4 + x5 + x6) % 2 == 0 and \
                               (x4 + x5 + x6 + x7) % 2 == 1:
                                solutions.append((x1, x2, x3, x4, x5, x6, x7))

for solution in solutions:
    print(solution)
