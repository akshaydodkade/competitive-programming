for i in range(int(input())): # T
  N = int(input())
  A = list(map(int, input().split()))

  max = A[0]
  for j in range(1, len(A)):
    if A[j] > max:
      max = A[j]

  print(max)