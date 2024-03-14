for T in range(int(input())): # T
  A = list(input())

  A_first = A[:len(A) // 2]
  if len(A) % 2 == 1:
    A_last = A[(len(A) // 2) + 1:]
  else:
    A_last = A[len(A) // 2:]

  print('YES' if sorted(A_first) == sorted(A_last) else 'NO')