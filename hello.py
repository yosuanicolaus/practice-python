def solve(M, N):
    for i in range(M, N + 1):
        if i == 1: continue
        red_flag = False
        for k in range(2, int(i/2) + 1):
            if i % k == 0:
                # not prime
                red_flag = True
                break
        if red_flag: continue
        print(i)



def main():
    T = int(input())
    for tc in range(T):
        M, N = map(int, input().split())

        solve(M, N)


main()
