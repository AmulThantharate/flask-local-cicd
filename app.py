from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/tasks")
@app.get("/api/tasks")
def get_tasks():
    return jsonify(tasks), 200


@app.post("/tasks")
@app.post("/api/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"message": "title is required"}), 400

    task = {"id": len(tasks) + 1, "title": title.strip()}

    tasks.append(task)
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
