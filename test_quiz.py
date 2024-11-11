# tests/test_quiz.py
from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService

# Test for creating a new quiz
@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    # INCOMPLETE: Set up the mock return value
    # TODO: Set `mock_create_quiz.return_value` to 1 (a mock quiz ID)
    mock_create_quiz.return_value = 1

   # INCOMPLETE: Make a POST request to create a quiz
    # TODO: Use `client.post` to send a POST request to `/api/quizzes` with JSON data
    data = {"title": "Sample Quiz", "questions": [{"text": "What is 1 + 2?", "answer": "3"}]}
    response = client.post('/api/quizzes', json=data)
    
    # INCOMPLETE: Write assertions to check the response
    # TODO: Assert that status code is 201, `quiz_id` in response is 1, and `mock_create_quiz` was called once
    assert response.status_code == 201
    assert response.json['quiz_id'] == 1
    mock_create_quiz.assert_called_once()

# Test for retrieving a quiz by ID
@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    # Setting up the mock to simulate a QuizModel object
    mock_quiz = MagicMock()
    mock_quiz.title = "Sample Quiz"
    # Ensure the dictionary keys here match what you use in the controller
    mock_quiz.questions = [{"question": "What is 1 + 2?", "answer": "3"}]

    # Assign the mock quiz to `mock_get_quiz.return_value`
    mock_get_quiz.return_value = mock_quiz

    # Make a GET request to retrieve the quiz
    response = client.get('/api/quizzes/1')

    # Write assertions to check the response
    assert response.status_code == 200
    assert response.json['title'] == "Sample Quiz"
    assert response.json['questions'] == [{"text": "What is 1 + 2?", "answer": "3"}]
    mock_get_quiz.assert_called_once_with(1)

# Test for submitting answers and evaluating a quiz
@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    # INCOMPLETE: Set up the mock to simulate score calculation
    # TODO: Set `mock_evaluate_quiz.return_value` to (1, "Quiz evaluated successfully")
    mock_evaluate_quiz.return_value = (1, "Quiz evaluated successfully")

    # INCOMPLETE: Make a POST request to submit answers for a quiz
    # TODO: Use `client.post` to send a POST request to `/api/quizzes/1/submit` with JSON data containing answers
    data = {"answers": ["3"]}
    response = client.post('/api/quizzes/1/submit', json=data)

    # INCOMPLETE: Write assertions to check the response
    # TODO: Assert that status code is 200, `score` in response is 1, `message` is "Quiz evaluated successfully", and `mock_evaluate_quiz` was called once
    pass  # REMOVE when implementing
    assert response.status_code == 200
    assert response.json['score'] == 1
    assert response.json['message'] == "Quiz evaluated successfully"
    mock_evaluate_quiz.assert_called_once_with(1, ["3"])
