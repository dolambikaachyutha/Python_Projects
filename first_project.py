import json
import os

filename="students_info.json"

def load_data():
    if  not os.path.exists(filename):
        return []
    
    with open(filename,"r") as f:
        return json.load(f)
    
def save_data(data):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4)

def add_student(data):
    
    student_id=input("enter student id:")
    for student in data:
        if student["id"]== student_id:
            print("student id exists already")
            return
    student_name=input("enter student name:")
    student_age=input("enter student age:")
    student_class=input("enter student calss:")

    math_marks=float(input("enter math marks:"))
    english_marks=float(input("enter english marks:"))
    science_marks=float(input("enter science marks:"))

    student_info={
        "id":student_id,
        "name":student_name,
        "age":student_age,
        "class":student_class,
        "marks":{
            "math":math_marks,
            "english":english_marks,
            "science":science_marks
        }
    }

    data.append(student_info)
    save_data(data)
    print("student added successfully")

def view_student(data):
    if not data:
        print("no data found")
        return
    for s in data:
        print(f"id: {s["id"]}")
        print(f"name: {s["name"]}")
        print(f"age: {s["age"]}")
        print(f"class: {s["class"]}")
        print(f"marks: {s["marks"]}")

def search_student(data):
    student_id=input("enter student id ")
    for s in data:
        if s["id"]== student_id:
            print("student found:")
            print(f"id: {s["id"]}")
            print(f"name: {s["name"]}")
            print(f"age: {s["age"]}")
            print(f"class: {s["class"]}")
            print(f"marks: {s["marks"]}")
            return s
    print("student not found")
    return None

def update_student_info(data):
    student_id=input("enter student id:")
    for s in data:
        if s["id"]== student_id:
            print("leave blank if you don't change the value, press enter.")

            name=input("enter new name:")
            age=int(input("enter new age:"))
            student_class=input("enter new class:")

            math=float(input("enter new maths marks:"))
            science=float(input("enter new science marks:"))
            english=float(input("enter new english marks:"))

            if name:
                s["name"]=name
            if age:
                s["age"]=age
            if student_class:
                s["class"]=student_class
            if math:
                s["marks"]["math"]=float(math)
            if science:
                s["marks"]["science"]=float(science)
            if english:
                s["marks"]["english"]=float(english)
            save_data(data)
            return
    print("student not found") 

def delete_student(data):
    student_id=input("enter student id for delete student:")
    for s in data:
        if s["id"]==student_id:
            data.remove(s)

            save_data(data)
            print("student info delete successfully")
            return
        print("student id not found")
def calculate_percentege(s):
    marks=s["marks"]

    total=(
        marks["math"]+
        marks["science"]+
        marks["english"]

    )

    percentege=total/3
    return percentege

def calculate_grade(percentege):
    if percentege >=90:
        return "A"
    elif percentege >= 75 and percentege < 90:
        return "B"
    elif percentege >= 60 and percentege <75:
        return  "c"
    elif percentege >=40 and percentege <60:
        return "D"
    else:
        return "F"

def genrate_report_card(data):
    student_id=input("enter student id for report card")
    for s in data:
        if s["id"]==student_id:

            percentage=calculate_percentege(s)
            grade=calculate_grade(percentage)
            
            print("\n=====REPORT CARD====")

            print(f"id : {s["id"]}")
            print(f"name :{s["name"]}")
            print(f"class : {s["class"]}")

            print("\n====MARKS===")

            print(f"math : {s["marks"]["math"]}")
            print(f"math : {s["marks"]["science"]}")
            print(f"math : {s["marks"]["english"]}")

            print("\n----------")

            print(f"percentage: {round(percentage,2)}%")
            print(f"grade: {grade}")
            
            return
        print("student id not found")

def mein():
    data=load_data()

    while True:
        print("------School management system-----")

        print("1. ADD_STUDENT:")
        print("2. VIEW_STUDENT")
        print("3. SEARCH_STUDENT:")
        print("4. UPDATE_STUDENT_INFO:")
        print("5. DELETE_STUDENT_INFO:")
        print("6. GENRATE_REPORT_CARD:")
        print("7. EXIT")

        choice=input("enter your choice:(1,2,3,4,5,6,7): ")
        if choice=="1":
            add_student(data)
        elif choice=="2":
            view_student(data)
        elif choice =="3":
            search_student(data)
        elif choice =="4":
            update_student_info(data)
        elif choice =="5":
            delete_student(data)
        elif choice=="6":
            genrate_report_card(data)
        elif choice=="7":
            print("program exited")
            break
        else:
            print("invalid input")

mein()


 

            
         







