# Method to find all the cavities on the map and replace their depths with the uppercase character X
def cavityMap(grid):
    for i in range(1 , len(grid) - 1):
        for j in range(1 , len(grid) - 1):
            if(grid[i][j] > max(grid[i-1][j] , grid[i][j-1] , grid[i][j+1] , grid[i+1][j])):
                grid[i] = grid[i][0 : j] + 'X' + grid[i][j + 1 : n]
    print(*grid)

# Program Test
if __name__ == '__main__':
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)