from bisect import bisect_left as bs
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    l1, note1 = int(input()), [int(x) for x in input().split()]
    note1.sort()

    l2, note2 = int(input()), [int(x) for x in input().split()]

    def in_note1(x):
        i = bs(note1, x)
        return note1[i if i < l1 else -1] == x

    for x in note2:
        print(1 if in_note1(x) else 0)