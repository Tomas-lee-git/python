# pytest 会测试所在文件目录的所有测试文件；
# pytest file_name.py 可以专注于一个测试文件；

from survey import AnonymousSurvey as As

def test_survey_instance_object_attribute():
    """测试实例对象的属性是否正常"""
    question = "What language did you first learn to speak?"
    language_survey = As(question)
    assert language_survey.question == question

def test_store_single_response():
    """测试单个答案会被妥善地存储"""
    question = "What language did you first learn to speak?"
    language_survey = As(question)
    language_survey.store_response("Chinese")
    # 有，且只有这一个答案
    assert "Chinese" in language_survey.responses
    assert len(language_survey.responses) == 1

def test_store_three_responses():
    """测试三个答案会被妥善地存储"""
    question = "What language did you first learn to speak?"
    language_survey = As(question)
    responses = ["Chinese", "English", "Japanese"]
    for response in responses:
        language_survey.store_response(response)
    # 都有，且有三个答案
    assert len(language_survey.responses) == 3
    for response in responses:
        assert response in language_survey.responses