namespaces = {'global': None}
variable = {'global': set()}

def create(namesp, parent):
    namespaces[namesp] = parent
    variable[namesp] = set()

def add(namesp, arg):
    variable[namesp].add(arg)

def get(namesp, arg):
    if arg in variable[namesp]:
        print(namesp)
    elif namesp == 'global' and arg not in variable['global']:
        print('None')
    else:
        get(namespaces[namesp],arg)

n = int(input())
for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
        print(namespaces)
        print(variable)
    if cmd == 'add':
        add(namesp, arg)
        print(namespaces)
        print(variable)
    if cmd == 'get':
        get(namesp, arg)
        print(namespaces)
        print(variable)
