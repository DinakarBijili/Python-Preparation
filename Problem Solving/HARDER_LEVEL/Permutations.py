"""Permutation [Premium]"""
def get_permutation(lst):
    if len(lst) == 0 :
        return []
    if len(lst) == 1 :
        return [lst]
    permutation = [ ]
    for i in range(len(lst)):
        current = lst[i]
        rem_list = lst[:i] + lst[i+1:]
        rem_perm = get_permutation(rem_list)
        for p in rem_perm:
            permutation.append([current]+p)
    return permutation
data = [1,2,3]
for permutation in get_permutation(data):
    print(permutation)