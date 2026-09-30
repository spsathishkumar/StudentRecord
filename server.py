from flask import Flask, jsonify, request

app = Flask(__name__)

# Create student data name, age, id, and mark
students = [
    {"name": "Alice", "age": 20, "id": 1, "mark": 85},
    {"name": "Bob", "age": 22, "id": 2, "mark": 90},
    {"name": "Charlie", "age": 21, "id": 3, "mark": 78},
    {"name": "David", "age": 26, "id": 4, "mark": 84}
]

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Student API!"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    #use for loop to find student by id
    student = None
    for s in students:
        if s["id"] == student_id:
            student = s
            break
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

# Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = {
        "name": data["name"],
        "age": data["age"],
        "id": len(students) + 1,
        "mark": data["mark"]
    }
    students.append(new_student)
    return jsonify(new_student), 201

# Update a student's information
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    #use for loop to find student by id
    student = None
    for s in students:
        if s["id"] == student_id:
            student = s
            break
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    student.update({
        "name": data.get("name", student["name"]),
        "age": data.get("age", student["age"]),
        "mark": data.get("mark", student["mark"])
    })
    return jsonify(student)

# Delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)