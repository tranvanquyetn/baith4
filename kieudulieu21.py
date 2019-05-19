value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
 intp = int(p, 2)
 if not intp%5:
  value.append(p)
# Bài tập Python 14, Code by Quantrimang.com
print (','.join(value))