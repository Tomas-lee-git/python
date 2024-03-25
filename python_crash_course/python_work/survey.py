"""
    测试中常用的断言语句:
        1. ==, 断言两个值相等；
        2. !=, 断言两个值不相等；
        3. a, 断言 a 的布尔值为 True；
        4. not a, 断言 a 的布尔值为 False；
        5. element in list/str 断言元素在列表、字符串中；
        6. element not in list/str 断言元素不在列表、字符串中；
    测试能包含任意可用条件语句表示的断言
"""
class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答案"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")
