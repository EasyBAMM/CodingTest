# book - Tct 10장 (경로 압축 기법 서로소 집합)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
