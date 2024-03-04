for i in range(int(input())):
  l = []
  for j in range(int(input())):
    n = int(input())

    if n in l:
      l.remove(n)
    else:
      l.append(n)
  print(l[0])
  