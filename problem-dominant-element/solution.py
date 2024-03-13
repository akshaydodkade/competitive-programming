for i in range(int(input())): # T
  N = int(input())
  A = list(map(int, input().split()))

  freq = {}
  for num in A:
    freq[num] = freq.get(num, 0) + 1
  
  max_freq = max(freq.values())
  freq_list = list(freq.values())

  if(freq_list.count(max_freq) > 1):
    print('NO')
  else:
    print('YES')
