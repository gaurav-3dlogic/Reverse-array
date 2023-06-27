def revarray(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1

a = [1, 2, 3]
revarray(a, 0, 2)
print(a)

#Time complixty - 0(n)
# space complixty - 0(1)
