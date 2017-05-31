#!/usr/bin/env python3.4

from union_find import UnionFind


def main():
    uf = UnionFind()
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        uf.union(a, b)
    uf.print_components()


if __name__ == '__main__':
    main()
