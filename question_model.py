class Model:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer   
        self.question = {
            "q_text" : self.text,
            "q_answer" : self.answer,
        }     