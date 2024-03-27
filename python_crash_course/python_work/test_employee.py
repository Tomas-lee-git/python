import pytest
from employee import Employee

@pytest.fixture
def eric():
    """多次重复的测试资源，提出来，做成夹具"""
    return Employee("eric", "hua", 250000)

def test_give_raise_500(eric):
    """加五百羞辱一下你"""
    eric.give_raise(500)
    assert eric.salary == 250000 + 500

def test_give_raise_default(eric):
    """逗你呢，我们要加就加30%"""
    eric.give_raise()
    assert eric.salary == 250000 * 1.3

def test_double_up(eric):
    """干的不错，薪水翻倍"""
    eric.double_up()
    assert eric.salary == 250000 * 2
    