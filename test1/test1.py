from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Öğle yemeğini ye", "done": False},
    {"id": 2, "title": "Projeyi tamamla", "done": True},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    task_data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": task_data["title"],
        "done": task_data.get("done", False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        tasks.remove(task)
        return '', 204
    return jsonify({"message": "Görev bulunamadı"}), 404

if __name__ == '__main__':
    app.run(debug=True)
