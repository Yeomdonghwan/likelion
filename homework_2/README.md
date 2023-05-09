# homework2

## 학생 관리 프로그램

학생 CRUD (Create, Read, Update, Delete) 기능을 구현하기.

파일 목록
- main.py
- Student.py
- StudentManagerRepo.py
- StudentManagerImpl.py
- StudentManagerService.py
---

## 간략 설명
1. main에서 사용자에게 메뉴 선택을 받습니다.
2. 각 메뉴에 따라 추가적으로 필요한 입력을 받고(학생 추가시 새로운 학생의 정보 등), StudentManagerService 객체가 비즈니스 로직을 처리하도록 요청합니다.
3. StudentManagerService는 유효성 검사 등의 비즈니스 로직을 처리하며, StudentManagerImpl 객체를 통해 데이터베이스(리스트) 작업을 요청합니다
4. StudentManagerImpl는 데이터베이스(리스트)에 접근하여 학생 정보를 추가,조회,수정,삭제 등 데이터를 처리합니다.

---
[리뷰](https://github.com/Yeomdonghwan/likelion/blob/master/homework_2/review.md)
