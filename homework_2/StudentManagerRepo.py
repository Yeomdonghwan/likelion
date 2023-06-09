
from abc import abstractmethod


class StudentManagerRepo:
    @abstractmethod
    def add_student(self, student): # 학생 추가
        pass

    @abstractmethod
    def recieve_student(self): # 학생 출력
        pass

    @abstractmethod
    def list_student(self): # 전체 학생 조회
        pass

    @abstractmethod
    def search_student(self, name): # 학생 조회
        pass

    @abstractmethod
    def delete_student(self, name): # 학생 제거
        pass

    @abstractmethod
    def update_student(self, name, student): # 학생 수정
        pass

    