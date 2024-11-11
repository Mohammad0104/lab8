from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')


@quiz_bp.route('', methods=['POST'])
def create_quiz():
    # Initialize the QuizService
    service = QuizService()

    # Retrieve JSON data from the request
    data = request.json

    # Call the create_quiz method in the service
    quiz_id = service.create_quiz(data)

    # Return a JSON response with the quiz ID and a 201 status
    return jsonify({"message": "Quiz created", "quiz_id": quiz_id}), 201


@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    # Initialize the QuizService
    service = QuizService()

    # Use the service to retrieve the quiz by its ID
    quiz = service.get_quiz(quiz_id)

    # Check if the quiz exists and return a JSON response
    if quiz:
        questions = [
            {"text": question["text"], "answer": question["answer"]}
            for question in quiz.questions
        ]
        response_data = {
            "title": quiz.title,
            "questions": questions
        }
        return jsonify(response_data), 200
    else:
        return jsonify({"message": "Quiz not found"}), 404


@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    # Initialize the QuizService
    service = QuizService()

    # Retrieve answers from the request JSON
    user_answers = request.json.get('answers')

    # Use the service to evaluate the quiz with the provided answers
    score, message = service.evaluate_quiz(quiz_id, user_answers)

    # Check if evaluation was successful and return the response
    if score is None:
        return jsonify({"message": "Quiz not found"}), 404
    else:
        return jsonify({"score": score, "message": message}), 200
