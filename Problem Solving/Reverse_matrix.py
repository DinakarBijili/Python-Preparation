"""Reverse matrix"""
def reverse_matrix(m):
    m.reverse()
    for row in m:
        row.reverse()
mat = [[1,2],[2,4],[5,9]]
reverse_matrix(mat)
print(mat)