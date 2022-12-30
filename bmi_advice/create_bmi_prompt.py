class CreateBmiPrompt:
    def __init__(self, sex="female", bmi=26, age=25):
        self.sex = sex
        self.bmi = bmi
        self.age = age

    def createPrompt(self):
        prompt = f"Give a weight-related advice to a person that is {self.sex}, has a bmi of {self.bmi} and is {self.age} years old."
        return prompt
