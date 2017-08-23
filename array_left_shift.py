def array_left_rotation(a, n, k):
    d_array = a[0 : k]
    r_array = a[k : n]
    return r_array + d_array

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
