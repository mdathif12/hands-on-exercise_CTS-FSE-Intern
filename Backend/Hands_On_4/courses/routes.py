from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    'courses',
    __name__,
    url_prefix='/api/courses'
)

courses = []


def make_response_json(data, status_code=200):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():
    return make_response_json(courses)


@courses_bp.route('/', methods=['POST'])
def create_course():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "JSON data required"
        }), 400

    required_fields = ['name', 'code', 'credits']

    for field in required_fields:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"{field} is required"
            }), 400

    course = {
        "id": len(courses) + 1,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"]
    }

    courses.append(course)

    return make_response_json(course, 201)


@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):

    course = next(
        (c for c in courses if c["id"] == course_id),
        None
    )

    if not course:
        return jsonify({
            "status": "error",
            "message": "Course not found"
        }), 404

    return make_response_json(course)


@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):

    course = next(
        (c for c in courses if c["id"] == course_id),
        None
    )

    if not course:
        return jsonify({
            "status": "error",
            "message": "Course not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "JSON data required"
        }), 400

    course["name"] = data.get("name", course["name"])
    course["code"] = data.get("code", course["code"])
    course["credits"] = data.get("credits", course["credits"])

    return make_response_json(course)


@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):

    course = next(
        (c for c in courses if c["id"] == course_id),
        None
    )

    if not course:
        return jsonify({
            "status": "error",
            "message": "Course not found"
        }), 404

    courses.remove(course)

    return make_response_json({
        "message": "Course deleted successfully"
    })