def or_gate(x1, x2):
    w1 = 4
    w2 = 4
    T = 2
    # 0 > T : False => T >= 0
    # w1 > T
    # w2 > T
    # w1 + w2 > T
    # T = 0.3, w1 = 0.4, w2 = 0.4
    # result = x1*w1 + x2*w2 > T
    # print(result)
    return int(x1*w1 + x2*w2 > T)


def and_gate(x1, x2):
    w1 = 3
    w2 = 3
    T = 5
    # 0 > T : False => T >= 0
    # w1 > T : False => T >= w1
    # w2 > T : False => T >= w2
    # w1 + w2 > T
    return int(x1*w1 + x2*w2 > T)


def mc_cul_net():
    inputs = ((0, 0), (0, 1), (1, 0), (1, 1))

    print("***** OR GATE *****")
    print(f"x1   x2   y")
    for x1, x2 in inputs:
        print(f"{x1}    {x2}    {or_gate(x1, x2)}")
    print("\n***** AND GATE *****")
    print("x1   x2   y")
    for x1, x2 in inputs:
        print(f"{x1}    {x2}    {and_gate(x1, x2)}" )
