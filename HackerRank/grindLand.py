def gridLand(inp):
    final_res = []
    for in_str in inp:
        goal_x, goal_y, k =  in_str.split()
        goal_x = int(goal_x)
        goal_y = int(goal_y)
        k      = int(k)
        res = []
        dfs(res, 0, 0, goal_x, goal_y, "")
        final_res.append(res[k])
    return final_res

def dfs(res, curr_x, curr_y, goal_x, goal_y, path):
    if curr_x <= goal_x and curr_y <= goal_y:
        if curr_x == goal_x and curr_y == goal_y:
            res.append(path)
            return
        if curr_x < goal_x:
            dfs(res, curr_x + 1, curr_y, goal_x, goal_y, path + "H")
        if curr_y < goal_y:
            dfs(res, curr_x, curr_y + 1, goal_x, goal_y, path + "V")

if __name__ == "__main__":
    print gridLand(["2 2 2", "2 2 3"])

