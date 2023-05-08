from StudentManagerService import StudentManagerService
from Student import Student
manager = StudentManagerService()


while(1):
    print("==========================================")
    print("1. 학생 추가")
    print("2. 학생 출력")
    print("3. 전체 학생 조회")
    print("4. 학생 제거")
    print("5. 학생 수정")
    print("6. 전체 학생 학점순 조회")
    print("7. 종료")
    print("=========================================")
    select = int(input("번호를 눌러주세요: "))
    if(select==1): #학생 추가
        name=input("이름: ")
        studentId=input("학번: ")
        age=input("나이: ")
        major=input("전공: ")
        gpa=input("학점: ")
        manager.add_student(Student(studentId,name,age,major,gpa))

    elif(select==2): #학생 출력
        name=input("이름: ")
        manager.search_student(name)

    elif(select==3): #전체 학생 조회
        manager.list_student()
        
    elif(select==4): #학생 제거
        name=input("이름: ")
        manager.delete_student(name)

    elif(select==5): #학생 수정
        name=input("이름: ")
        studentId=input("학번: ")
        age=input("나이: ")
        major=input("전공: ")
        gpa=input("학점: ")
        manager.update_student(name,Student(studentId,name,age,major,gpa))
        
    elif(select==6): #학점순 정렬 조회
        manager.list_student_by_gpa()
        
    else: #종료
        break
        
    
    

    