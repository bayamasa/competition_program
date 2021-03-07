N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int , input().split)
    A.append(a)
    B.append(b)

i = A.index(min(A))
j = B.index(min(B))

if i == j:
  a, b = A[i], B[i]
  del A[i]
  del B[i]
  ans = min(a + b, max(min(A), b), max(a, min(B)))
else:
  ans = max(A[i], B[j])

print(ans)
