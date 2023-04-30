import pandas as pd
from pathlib import Path
import logging

from quiz.question import Question

_logger = logging.getLogger(__name__)


class Sheet:
    
    def __init__(self, n: int, df: pd.DataFrame) -> None:
        self._number = n
        self._df = df
        self._questions = []

    def generate_quiz(self):
        _logger.info(f"Generating quiz for student #{self.number}")
        for row in self.df.itertuples(index=False):
            alts = self.df['capital'].sample(n=3).to_list()
            _logger.debug(f"Generating question for {row[0]} with ans={row[1]}")
            q = Question(query=row[0], answer=row[1], alts=alts)
            self._questions.append(q)

    @property
    def number(self):
        return self._number
    
    @property
    def df(self):
        return self._df
    
    @property
    def questions(self):
        return self._questions