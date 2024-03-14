for T in range(int(input())): # T
  A = list(input())

  # remove middle element for odd length array
  if len(A) % 2 == 1:
    A.pop(len(A) // 2)

  A_first = A[:len(A) // 2]
  A_last = A[len(A) // 2:]

  for i in range(len(A) // 2):
    if A_first.count(A[i]) > 0:
      A_first.remove(A[i])
    if A_last.count(A[i]) > 0:
      A_last.remove(A[i])

  if len(A_first) == 0 and len(A_last) == 0:
    print('YES')
  else:
    print('NO')