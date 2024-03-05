for i in range(int(input())): #fetch test cases T
  n = int(input()) #get number of friends
  d = list(set(map(int, input().split())))
  print(len(d))
