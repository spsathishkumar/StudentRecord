import requests

class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        response.raise_for_status()
        return response.status_code

# Example usage:
if __name__ == "__main__":
    client = Client("http://localhost:5000")
    # Get all students
    students = client.get("students")
    print(students)
    # Get a specific student
    student = client.get("students/1")
    print(student)
    # Add a new student
    new_student = {
        "name": "David",
        "age": 23,
        "mark": 88
    }
    added_student = client.post("students", data=new_student)
    print(added_student)
    # Update a student's information
    updated_student = {
        "name": "David Updated",
        "age": 24,
        "mark": 90
    }
    updated = client.put("students/1", data=updated_student)
    print(updated)
    # Delete a student
    delete_status = client.delete("students/1")
    print(delete_status)
    