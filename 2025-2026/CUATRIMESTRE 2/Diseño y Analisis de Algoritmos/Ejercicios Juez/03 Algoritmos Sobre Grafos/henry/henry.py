N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

visited = [[[False]*2 for _ in range(M)] for _ in range(N)] #no lo tengo porque usar ya que no me puedo mover en diagonal y la paridad al llegar a cada casilla siempre va a ser la misma, pero lo hago por poder adaptar la solución a grafos de movimiento más generales
# parity = 1 -> turno impar, parity = 0 -> turno par
q = []
q.append((0, 0, 1, 0)) #x,y,paridad del turno actual, distancia
visited[0][0][1] = True
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while q:
    x, y, parity, dist = q.pop(0)
    if maze[x][y] == 2:
        print(dist)
        break
    nextParity = dist % 2 #calcular paridad del siguiente piso
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M: #respeta los margenes
            # En turno impar se puede entrar en cualquier casilla en turno par solo en las que no son muro
            if parity== 1 or maze[nx][ny] != -1:
                if not visited[nx][ny][nextParity]:
                    visited[nx][ny][nextParity] = True
                    q.append((nx, ny, nextParity, dist + 1))