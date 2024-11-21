# Solution not optimized but it works for test cases
class SolutionDraft(object):
    def countUnguarded(m, n, guards, walls):
        grid = [['.'] * n for _ in range(m)]
        for x, y in guards:
            grid[x][y] = 'G'
        for x, y in walls:
            grid[x][y] = 'W'

        for valueGLine in range(m):
            for valueGColumn in range(n):
                if grid[valueGLine][valueGColumn] == 'G':

                    for i in range(valueGLine+1, m):
                        if grid[i][valueGColumn] == 'W' or grid[i][valueGColumn] == 'G':
                            break
                        grid[i][valueGColumn] = 'U'
                    

                    for i in range(valueGLine-1, -1, -1):
                        if grid[i][valueGColumn] == 'W' or grid[i][valueGColumn] == 'G':
                            break
                        grid[i][valueGColumn] = 'U'


                    for i in range(valueGColumn+1, n):
                        if grid[valueGLine][i] == 'W' or grid[valueGLine][i] == 'G':
                            break
                        grid[valueGLine][i] = 'U'


                    for i in range(valueGColumn-1, -1, -1):
                        if grid[valueGLine][i] == 'W' or grid[valueGLine][i] == 'G':
                            break
                        grid[valueGLine][i] = 'U'

        return sum(row.count('.') for row in grid)


#Solution Optimized
class Solution(object):
    def countUnguarded(m, n, guards, walls):
        grid = [['.'] * n for _ in range(m)]
        guard_set = set((x, y) for x, y in guards)
        wall_set = set((x, y) for x, y in walls)

        for x, y in guards:
            grid[x][y] = 'G'
        for x, y in walls:
            grid[x][y] = 'W'

        def mark_direction(x, y, dx, dy):
            while 0 <= x < m and 0 <= y < n:
                if (x, y) in guard_set or (x, y) in wall_set:
                    break
                grid[x][y] = 'U'
                x += dx
                y += dy

        for x, y in guards:
            mark_direction(x + 1, y, 1, 0)
            mark_direction(x - 1, y, -1, 0)
            mark_direction(x, y + 1, 0, 1)
            mark_direction(x, y - 1, 0, -1)

        return sum(row.count('.') for row in grid)
    


Solution.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]])
Solution.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]])
