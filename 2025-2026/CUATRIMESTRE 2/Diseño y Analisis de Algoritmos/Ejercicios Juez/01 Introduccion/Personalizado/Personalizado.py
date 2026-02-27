N = int(input())
team = []
for i in range(N):
    name, age = input().split()
    team.append([name, int(age)])

team.sort(key=lambda x: x[1], reverse=True)
leader = team.pop(0)
if len(team) != 1:
    print('Bienvenido equipo de', leader[0], 'compuesto por',len(team), 'personas')
else:
    print('Bienvenido equipo de', leader[0], 'compuesto por 1 persona')

