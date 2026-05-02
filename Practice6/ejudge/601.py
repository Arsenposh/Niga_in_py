n=int(input())

num= list(map(int, input().split()))

sq = map(lambda x: x*x, num)

print(sum(sq))