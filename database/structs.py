from enum import Enum
from typing import List, Set
# from db_manager import db_matches, db_reqs, db_user


subjects = {
    "maths": 0,
    "physics": 1,
    "chemistry" : 2,
    "biology": 3,
    "english": 4,
    "history": 5,
    "geography": 6,
    "russian": 7,
    "social_studies": 8,
    "economics": 9,
    "literature": 10,
    "art": 11,
    "linear_algebra": 12,
    "calculus": 13,
    "statistics": 14,
    "computer_science": 15
}


class Tutor:
    def __init__(self, id_: int, name_: str, subjects_: Set[int], grade_: int) -> None:
        self.id = id_
        self.name = name_
        self.subjects = set()
        self.grade = grade_
        for el in subjects_:
            self.subjects.add((el))
        # db_user.add_user(self)


    def add_subject(self, subject: int) -> None:
        self.subjects.add(subject)
        # db_user.update_user_subjects(self.id, self.subjects)
    
    def remove_subject(self, subject: int) -> None:
        self.subjects.remove(subject)
        # db_user.update_user_subjects(self.id, self.subjects)

    def __str__(self) -> str:
        return f"Tutor(id={self.id}, name={self.name}, subjects={self.subjects}, grade={self.grade})"
