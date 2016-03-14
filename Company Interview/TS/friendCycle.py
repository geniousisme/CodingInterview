# Heard that it is called union find...berkely algorithm class week 1 content
# need to study more.
def get_relationship_matrix(friends):
    relation_matrix = []
    for friend in friends:
        relation_matrix.append(list(friend))
    return relation_matrix

def is_connected(id_list, idx1, idx2):
    return id_list[idx1] == id_list[idx2]

def union(id_list, idx1, idx2, friend_cycle_count):
    id1, id2 = id_list[idx1], id_list[idx2]
    for i in xrange(len(id_list)):
        if id_list[i] == idx1:
           id_list[i] = idx2
           friend_cycle_count -= 1
    return friend_cycle_count

def friendCircles(friends):
    id_list = []
    relation_matrix = get_relationship_matrix(friends)
    friend_cycle_count = len(friends)
    for i in xrange(friend_cycle_count):
        id_list.append(i)
    for i in xrange(friend_cycle_count):
        for j in xrange(i):
            if relation_matrix[i][j] == 'Y' and not is_connected(id_list, i, j):
                friend_cycle_count = union(id_list, i, j, friend_cycle_count)
    return friend_cycle_count

if __name__ == "__main__":
    friends1 = ["YYNN", "YYYN", "NYYN", "NNNY"]
    print friendCircles(friends1)
    friends2 = ["YNNNN", "NYNNN", "NNYNN", "NNNYN", "NNNNY"]
    print friendCircles(friends2)
    friends3 = ["YYY", "YYY", "YYY"]
    print friendCircles(friends3)

