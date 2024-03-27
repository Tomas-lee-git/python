# pytest 会测试所在文件目录的所有测试文件；
# pytest file_name.py 可以专注于一个测试文件；
"""
    夹具（fixture）：
        1. 在测试中， 夹具可帮助我们搭建测试环境，这通常意味着创建共多个测试使用的资源，
            也就是把一些重复的代码提出来共用；
        2. 在 pytest 中，要创建夹具，可编写一个使用装饰器 @pytest.fixture 装饰的函数；
        3. 装饰器（decorator）是放在函数定义前面的指令，在运行函数前，Python 将该指令应用于
           函数，以修改函数代码的行为；
    
    夹具的具体使用：
        1. 发现多个测试函数中有共同依赖的测试资源；
        2. 编写一个函数 fn 来生成供多个测试函数使用的资源；
        3. 对这个函数应用装饰器 @pytest.fixture；
        4. 把这个函数名称 fn 作为形参，放进每个使用该资源的测试函数中；
        5. 删除之前各个测试函数中重复依赖的测试资源；
        6. ❕需要确保夹具的名称，形参的名称，原依赖资源的名称，三处保持完全一致；
        
    夹具的工作原理：
        1. 前提：当测试函数的一个形参与应用了装饰器 @pytest.fixture 的函数（夹具）同名时
        2. 运行：
            2.1. 自动运行夹具；
            2.2. 将夹具返回的值传递给测试函数；
"""

import pytest
from survey import AnonymousSurvey as As


@pytest.fixture
def language_survey():
    """可供所有测试函数共同使用的 As 实例"""
    question = "What language did you first learn to speak?"
    language_survey = As(question)
    return language_survey


def test_store_single_response(language_survey):
    """测试单个答案会被妥善地存储"""
    language_survey.store_response("Chinese")
    # 有，且只有这一个答案
    assert "Chinese" in language_survey.responses
    assert len(language_survey.responses) == 1


def test_store_three_responses(language_survey):
    """测试三个答案会被妥善地存储"""
    responses = ["Chinese", "English", "Japanese"]
    for response in responses:
        language_survey.store_response(response)
    # 都有，且有三个答案
    assert len(language_survey.responses) == 3
    for response in responses:
        assert response in language_survey.responses
