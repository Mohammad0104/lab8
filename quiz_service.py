from src.models.quiz_model import QuizModel


class QuizService:
    def create_quiz(self, quiz_data):
        # Extract `title` and `questions` from `quiz_data`
        title = quiz_data['title']
        questions = quiz_data['questions']

        # Create a new QuizModel instance
        quiz = QuizModel(
            title, questions
        )  # Initialize QuizModel with title and questions

        # Save the quiz and return its ID
        quiz.save()  # Save the quiz instance to the database
        return quiz.id  # Return the created quiz's ID

    def get_quiz(self, quiz_id):
        # Retrieve a quiz by its ID using the model
        return QuizModel.get_quiz(
            quiz_id
        )  # Use QuizModel's get_quiz method to retrieve and return the quiz

    def evaluate_quiz(self, quiz_id, user_answers):
        # Retrieve the quiz by its ID
        quiz = self.get_quiz(quiz_id)
        if not quiz:
            return None, "Quiz not found"

        # Calculate the score based on correct answers
        score = sum(
            1 for q, a in zip(quiz.questions, user_answers) if q['answer'] == a
        )
        return score, "Quiz evaluated successfully"
