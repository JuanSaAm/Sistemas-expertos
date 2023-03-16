from collections import deque

def depth_first_search(graph, node, goal, visited):
    if node == goal:
        return True

def bfs(graph, start, end):
    queue = deque()
    queue.append((start, [start]))

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None

Ejercicios = {}
Ejercicios['Distensión muscular'] = ['estiramiento de pantorrilla',' levantamiento de piernas','estiramiento de isquiotibiales','Yoga','calentamiento simple','estiramientos acuaticos','estiramiento de resistencia']
Ejercicios['Lesiones del manguito rotador'] = ['levantamiento de pesas ligeras','ejercicios de estiramiento','estiramiento de la pared','estiramiento de la mano detrás de la espalda','pesas sentado','Cardio','Estiramiento de brazos']
Ejercicios['Lesiones de ligamentos'] = ['fortalecimiento de los músculos', 'ejercicios de estabilidad', 'uso de una pelota de estabilidad','Equilibrio','Pesas','Ejercicios de respiración diafragmática']
Ejercicios['Lesiones de menisco'] = ['Estiramientos de cuello','Estiramientos de hombros','fortalecimiento de los músculos del manguito','Estiramientos de espalda','Ejercicios de fortalecimiento de la espalda','Estiramientos de cadera','Estiramientos de isquiotibiales']
Ejercicios['Espasmo muscular'] = ['fortalecimiento de los isquiotibiales','Estiramientos de rodilla','Estiramientos de tobillo','Ejercicios de fortalecimiento del tobillo','Ejercicios de equilibrio','Ejercicios de fortalecimiento de la pelvis']
Ejercicios['Tendinitis'] = ['Ejercicios de fortalecimiento del core','Estiramientos de codo','Ejercicios de fortalecimiento de codo','fortalecimiento de los músculos de la mano']

if __name__ == '__main__':
    token = str(input('Retroalimentacion\nQue Ejercicio haces?\n(Levatamiento de piernas, levantamiento de pesas, estiramiento del cuádriceps)\n'))
path = bfs(Ejercicios, 'Distension Muscular', token)
x = len(path)
print('Te recomiendo buscar libros del autor:',path[x-2])