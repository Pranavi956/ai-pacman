from flask import Flask, render_template, request, jsonify
from collections import deque

app = Flask(__name__)

# BFS AI for ghost
def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            x, y = node
            moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

            for move in moves:
                if 0 <= move[0] < 10 and 0 <= move[1] < 10:
                    new_path = list(path)
                    new_path.append(move)
                    queue.append(new_path)

    return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/move_ghost', methods=['POST'])
def move_ghost():
    data = request.json
    ghost = tuple(data['ghost'])
    pacman = tuple(data['pacman'])

    path = bfs(ghost, pacman)

    if len(path) > 1:
        next_move = path[1]
    else:
        next_move = ghost

    return jsonify({"ghost": next_move})

if __name__ == '__main__':
    app.run(debug=True)
