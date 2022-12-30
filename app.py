import bmi_advice as bmi
import openai
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

openai.api_key = "<insert_api_key>"

@app.route("/", methods=['GET', 'POST'])
def index():
  response = ""
  age = request.form.get("age")
  sex = request.form.get("sex")
  bmi_val = request.form.get("bmi")
  token = request.form.get("token")
  wrong_token = False
  if request.method == 'POST':
    if token == "<insert_local_token>":
      prompt = bmi.CreateBmiPrompt(sex,bmi_val,age)
      prompt_str = prompt.createPrompt()
      response = openai.Completion.create(model="text-davinci-003", 
                                      prompt=prompt_str, 
                                      temperature=0.7, 
                                      max_tokens=200, 
                                      top_p=1.0, 
                                      frequency_penalty=0.2, 
                                      presence_penalty=0.0)
      response = response["choices"][0]["text"]
    else:
      wrong_token = True
  return render_template("index.html",response=response,sex=sex, age=age,bmi=bmi_val, token=token, wrong_token = wrong_token)

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
  app.run(debug=True)

