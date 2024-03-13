for i in range(int(input())): # T
  N = int(input())
  A = list(map(int, input().split()))
  
  freq = {}
  for num in A:
    freq[num] = freq.get(num, 0) + 1

  max_count = max(freq.values())
  print(N - max_count)
