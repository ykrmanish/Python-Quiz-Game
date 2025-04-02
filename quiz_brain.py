import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        q_text = html.unescape(self.question_list[self.question_number]["q_text"])
        q_answer = self.question_list[self.question_number]["q_answer"]
        self.question_number+=1
        user_choice = input(f"Q.{self.question_number} {q_text}(True/Fasle)? ")
        
        if user_choice.lower() == q_answer.lower():
            print("You got that right🥳")
            self.score+=1
        else:
            print("You got that wrong🥲")
            print(f"Correct Answer: {q_answer}")
        print(f"Score: {self.score}/{self.question_number}\n")
        