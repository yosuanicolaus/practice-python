# only passed 1st test
# failed because I didn't consider scenario where s == 'aaabbbccc'
# in other words: we didn't get everything covered after all... ^^

def solve():
    pass


def main():
    t = int(input())
    for _ in range(t):
        n, k, m = map(int, input().split())
        s = input()
        alp = 'abcdefghijklmnopqrstuvwxyz'

        for ch in alp[:k]:
            if s.count(ch) < n:
                print('NO')
                print(ch * n)
                break
        else:
            print('YES')


if __name__ == "__main__":
    main()
