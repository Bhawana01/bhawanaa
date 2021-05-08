def compound_interest(principle, rate, time):
    # calculate CI
    CI = principle * (pow((1 + rate/100), time))
    print("Compound Interest is ", CI)

