from flask import Flask, request, Response
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://localhost:5001"
STUDENT_SERVICE = "http://localhost:5002"


@app.route('/api/courses', methods=['GET'])
@app.route('/api/courses/<path:path>', methods=['GET'])
def course_proxy(path=""):

    url = f"{COURSE_SERVICE}/api/courses"

    if path:
        url += f"/{path}"

    response = requests.request(
        method=request.method,
        url=url
    )

    return Response(
        response.content,
        response.status_code,
        response.headers.items()
    )


@app.route('/api/students', methods=['GET'])
@app.route('/api/students/<path:path>', methods=['GET', 'POST'])
def student_proxy(path=""):

    url = f"{STUDENT_SERVICE}/api/students"

    if path:
        url += f"/{path}"

    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json(silent=True)
    )

    return Response(
        response.content,
        response.status_code,
        response.headers.items()
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)