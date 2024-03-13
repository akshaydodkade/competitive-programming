for i in range(int(input())): # T
  N = int(input())
  A = list(map(int, input().split()))
  l = []
  max_count = 0
  for j in range(N):
    if A[j] in l: continue
    else: l.append(A[j])
    
    count = 0
    for k in range(N):
      if A[j] == A[k]:
        count += 1

    if count > max_count:
      max_count = count
      max_frequency = A[j]

  print(N - max_count)
