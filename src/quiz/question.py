import logging
from typing import Any, List
import numpy as np

_logger = logging.getLogger(__name__)

class Question:
    def __init__(self, query: str, answer: str, alts: List[str]) -> None:
        self._query = query
        self._answer = answer
        _logger.info(f'For query={self.query} and the answer={self.answer}')
        choice = ['A', 'B', 'C', 'D']
        self._answer_key = np.random.choice(choice,replace=False)
        choice.remove(self.answer_key)
        _logger.debug(f'answer_key={self.answer_key} and thus choice={choice}')
        self._question_key = {}
        self._question_key[self.answer_key] = self.answer
        for c in choice:
            self._question_key[c]=alts.pop()
        _logger.info(f'answer_key={self.answer_key},question_key={self.question_key}')

    @property
    def query(self):
        return self._query
    
    @property
    def answer(self):
        return self._answer
    
    @property
    def question_key(self):
        return self._question_key
    
    @property
    def answer_key(self):
        return self._answer_key
    
    @answer_key.setter
    def answer_key(self, value):
        self._answer_key = value
    

        
        

        