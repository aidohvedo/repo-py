a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


new_list = [a[s] for s in range(1,len(a))  if a[s] > a[s-1]]
print(new_list)