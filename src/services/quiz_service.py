from src.models.quiz_model import QuizModel

class QuizService:
    def create_quiz(self, quiz_data):
        # INCOMPLETE: Extract `title` and `questions` from `quiz_data`
        # TODO: Retrieve "title" and "questions" from `quiz_data` dictionary
        title = quiz_data['title']
        questions = quiz_data['questions']
        
        # INCOMPLETE: Create a new QuizModel instance
        # TODO: Initialize a QuizModel with `title` and `questions` (Hint: quiz = QuizModel(title, questions))
        quiz = QuizModel(title, questions)  # Initialize QuizModel with title and questions
        
        # INCOMPLETE: Save the quiz and return its ID
        # TODO: Call `save()` on the quiz instance and return `quiz.id`
        quiz.save()  # Save the quiz instance to the database
        return quiz.id  # Return the created quiz's ID

    def get_quiz(self, quiz_id):
        # INCOMPLETE: Retrieve a quiz by its ID using the model
        # TODO: Use QuizModel's `get_quiz` method to retrieve the quiz and return it
        return QuizModel.get_quiz(quiz_id)  # Use QuizModel's get_quiz method to retrieve and return the quiz

    def evaluate_quiz(self, quiz_id, user_answers):
        # INCOMPLETE: Retrieve the quiz by its ID
        # TODO: Call `get_quiz` with `quiz_id` and store the result in `quiz`
        quiz = self.get_quiz(quiz_id)  # Get the quiz using the provided quiz_id
        
        # INCOMPLETE: Check if the quiz exists
        # TODO: If `quiz` is None, return None and "Quiz not found"
        if not quiz:
            return None, "Quiz not found"  
        
        # INCOMPLETE: Calculate the score based on correct answers
        # TODO: Compare `user_answers` with `quiz.questions`, count correct answers, and return the score
        score = sum(1 for q, a in zip(quiz.questions, user_answers) if q['answer'] == a)
        return score, "Quiz evaluated successfully" 