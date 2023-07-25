import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Find the next question from the possible questions in the list.
    def next_question(self):
        self.current_question = self.question_list[self.question_number]            # Search for the question and convert it into a variable
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)                          # The html method is used to make the data downloaded from the API human-readable and free from codes
        return f"Q.{self.question_number}: {q_text}"                                # It returns the question and the response text

    # Checks the user's answer.
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer                               # Correct answer
        if user_answer.lower() == correct_answer.lower():                           # Compare correct answer with user's answer
            self.score += 1
            return True                                                             # If corrects score+1
        else:
            return False

