import math
def MinimalCost(n,  pairs):
    fused_group = []
    rod_hash = {}
    for pair in pairs:
        rod1, rod2 = pair.split()
        if rod_hash.get(rod1) is None:
            rod_hash[rod1] = [rod2]
        else:
            rod_hash[rod1].append(rod2)

    total_fused_num = 0
    cost = 0
    for rod, connected_rods in rod_hash.items():
        total_fused_num += 1 + len(connected_rods)
        cost += math.ceil(math.sqrt(len(connected_rods) + 1))
    return int((n - total_fused_num) + cost)

if __name__ == "__main__":
    print MinimalCost(4, ['1 2', '1 4'])






