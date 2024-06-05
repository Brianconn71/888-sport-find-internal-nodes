def find_internal_nodes_num(tree):
    internal_count = 0
    for i in range(len(tree)):
        if 0 <= tree[i] <= 6 and (
                (2 * i + 1 < len(tree) and tree[2 * i + 1]) or
                (2 * i + 2 < len(tree) and tree[2 * i + 2])
        ):
            internal_count += 1
    return internal_count

my_tree = [4, 4, 1, 5, -1, 4, 5]
print(find_internal_nodes_num(my_tree))
