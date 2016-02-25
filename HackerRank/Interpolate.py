

def Interpolate(n, amount, ucost):
    if not amount or not ucost:
        return 0
    amount_ucost_hash = {a:float(u) for a, u in zip(amount, ucost) if float(u) != 0}
    if len(amount_ucost_hash) == 1:
        return amount_ucost_hash.values()[0]
    elif amount_ucost_hash.get(n) is not None:
        return amount_ucost_hash[n]
    else:
        if n > amount[-1]:
            return extra_polate_ucost(amount_ucost_hash, n, amount[-1], amount[-2])
        elif n < amount[0]:
            return extra_polate_ucost(amount_ucost_hash, n, amount[0], amount[1])
        else: # find closet
            diff = float("inf")
            closet_ucost = 0
            for amount in amount_ucost_hash.keys():
                if abs(n - amount) < diff:
                    closet_ucost = amount_ucost_hash[amount]
            return round(n * float(closet_ucost) / amount, 2)

def extra_polate_ucost(amount_ucost_hash, new_amount, amount1, amount2):
    gradient = float(amount_ucost_hash[amount1] - amount_ucost_hash[amount2]) / (amount1 - amount2)
    closet_ucost1 = new_ucost(new_amount, amount1, amount_ucost_hash[amount1], gradient)
    closet_ucost2 = new_ucost(new_amount, amount2, amount_ucost_hash[amount2], gradient)
    return round((closet_ucost1 + closet_ucost2) * 0.5, 2)

def new_ucost(new_amount, old_amount, old_cost, gradient):
    return abs(old_amount - new_amount) * gradient + old_cost

if __name__ == "__main__":
    a = [10, 25, 100, 50, 500]
    u = ["0.0", "0.0", "54.25", "0.0", "0.0"]
    print Interpolate(100, a, u)

    a = [10, 25, 50, 100, 500]
    u = ["27.32", "23.13", "21.25", "18.00", "15.50"]
    print Interpolate(2000, a, u)