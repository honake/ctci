x = [1,1,0,-1,-1,-1,0,1]
y = [0,1,1,1,0,-1,-1,-1]
max_region = 0

def dfs(p,q):
    if grid[p][q] == 1:
        grid[p][q] = 0
        region = 1
        for dx, dy in zip(x,y):
            if 0 <= p+dx < n and 0 <= q+dy < m:
                region += dfs(p+dx,q+dy)
        return region
    elif grid[p][q] == 0:
        return 0

n = int(input().strip())
m = int(input().strip())
grid = []

for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)

for i in range(n):
    for j in range(m):
        max_region = max(max_region,dfs(i,j))

print(max_region)
