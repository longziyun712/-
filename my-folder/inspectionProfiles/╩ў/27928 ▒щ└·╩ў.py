from collections import defaultdict
import sys

sys.setrecursionlimit(10000)


def main():
    n = int(sys.stdin.readline())
    tree = defaultdict(list)
    all_nodes = set()
    child_nodes = set()

    for _ in range(n):
        parts = list(map(int, sys.stdin.readline().split()))
        parent, *children = parts
        tree[parent].extend(children)
        all_nodes.add(parent)
        all_nodes.update(children)
        child_nodes.update(children)

    # 根节点 = 出现在 all_nodes 但没出现在 child_nodes 的那个
    root = (all_nodes - child_nodes).pop()

    def traverse(u):
        # 把 u 自己和它的所有直接孩子放一起排序
        group = tree[u] + [u]
        group.sort()
        for x in group:
            if x == u:
                print(u)
            else:
                traverse(x)

    traverse(root)


if __name__ == "__main__":
    main()
