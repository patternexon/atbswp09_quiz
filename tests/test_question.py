import pytest
from unittest.mock import MagicMock
from quiz.question import Question

@pytest.fixture
def sample_question():
    return Question("New York", "Albany", ["x", "y", "z"])

def test_question_query_and_ans(sample_question: Question):
    assert "New York" == sample_question.query
    assert "Albany" == sample_question.answer
    assert "" == sample_question.question_key


