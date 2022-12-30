import bmi_advice as bmi
import openai
from flask import Flask, request

app = Flask(__name__)

openai.api_key = "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"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api")
def get_advice():
  sex = request.args.get('sex')
  bmi_val = request.args.get('bmi_val')
  age = request.args.get('age')
  prompt = bmi.CreateBmiPrompt(sex,bmi_val,age)
  prompt_str = prompt.createPrompt()
  response = openai.Completion.create(model="text-davinci-003", 
                                      prompt=prompt_str, 
                                      temperature=0.7, 
                                      max_tokens=200, 
                                      top_p=1.0, 
                                      frequency_penalty=0.2, 
                                      presence_penalty=0.0)
  return response["choices"][0]["text"]

if __name__ == '__main__':
  app.run()

