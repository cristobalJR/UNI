n,m = map(int,input().split())
maze=[[[]for _ in range(m)]for _ in range(n)]
start =[]
end =[]

for i in range(n):
    row = list(map(str,input().split()))
    for j in range(m):
        if row[j]=='s':
            start=[i,j]
            maze[i][j] = 's'
        elif row[j]=='e':
            end = [i,j]
            maze[i][j] = 'e'
        elif row[j]=='t':
            maze[i][j] = 'w'
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1),(1, 1),(-1, -1),(-1, 1),(1, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                        maze[ni][nj] = 'w'
        elif row[j]=='r':
            if maze[i][j]=='w':
                continue
            else:
                maze[i][j] = 'r'
        elif row[j]=='w':
            maze[i][j] = 'w'
        else:
            if maze[i][j]:
                continue
            else:
                maze[i][j] = 'f'
maze[start[0]][start[1]] = 's'
maze[end[0]][end[1]] = 'e'
rewards = sum(fila.count('r') for fila in maze)


path =[]
visited = [[False for _ in range(m)]for _ in range(n)]

mejor = float('inf')

def dfs(i, j, recogidas):
    global mejor
    if maze[i][j] == 'e':
        if recogidas == rewards:
            if len(path)<mejor:
                mejor = len(path)

        return

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != 'w' and not visited[ni][nj]:
            visited[ni][nj] = True        # marcar al entrar
            path.append([ni, nj])
            if maze[ni][nj] == 'r':
                dfs(ni, nj, recogidas + 1)
            else:dfs(ni, nj, recogidas)
            path.pop()                    # deshacer al salir(backtracking)
            visited[ni][nj] = False


visited[start[0]][start[1]] = True
path.append(start)
dfs(start[0], start[1], 0)
print(mejor)
