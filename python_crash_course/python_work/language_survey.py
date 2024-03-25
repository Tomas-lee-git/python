from survey import AnonymousSurvey as As

# 定义一个调查问卷的调查项目
question = "What language did you first learn to speak?"
# 创建一个表示调查的 As 的实例对象
language_survey = As(question)

# 显示问题并存储答案
language_survey.show_question()
print("Enter 'q' at any time to quit. ")
while True:
    response = input("Language: ")
    if response == "q":
        break
    else:
        language_survey.store_response(response)

# 调查结束后，显示调查结果
print("Thank you for everyone who participated in the survey!")
language_survey.show_results()
