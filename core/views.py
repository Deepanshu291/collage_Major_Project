from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import StudentDetail
import face_recognition as fc
import cv2
import numpy as np
import csv
import pandas as pd
from datetime import datetime


# Create your views here.
# @login_required(redirect_field_name='login')
# def home(req):
#     print(req.user)
#     form = StudentForm
#     if req.method == 'POST':
#         form = StudentForm(req.POST ,req.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context = {'form': form}
#     return render(req, 'index.html',context)

def addstudent(req):
    form = StudentForm
    if req.method == 'POST':
        form = StudentForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(req,'addstudent.html', context)

@login_required(redirect_field_name='login')
def home(req):
        # mentor = ProfessorDetail.objects.get(user= req.user) 
        # # print(mentor)
        # coursem = mentor.course.course
        # print(coursem)
        # students = StudentDetail.objects.filter(course=coursem)
        # df = pd.DataFrame(students)
        # return HttpResponse(df.to_html())
        course = Course.objects.all()
        if req.method == 'POST':
            coursef = req.POST['coursef']
            print(coursef)
            students = StudentDetail.objects.filter(course=coursef)
            print(students)
            context = {'courses':course,'students':students.order_by('enrollmentno')}
            return render(req,'index.html',context)
        context = {'courses':course}
        return render(req, 'index.html', context)
        
        


@login_required(redirect_field_name='login')
def display(req):
    now = datetime.now()
    currentdate =  now.strftime("%d-%b-%Y")
    f =open('media/csv/'+currentdate+'.csv','w+',newline='')
    csvwriter = csv.writer(f)
    csvwriter.writerow(['Roll no', 'Name', 'Mobile no', 'Status','Entry Time','Date'])
    # data=[]
    students = StudentDetail.objects.order_by('enrollmentno')
    for student in students:
        status = 'Present' if student.is_present else 'Absent'
        csvwriter.writerow([student.enrollmentno, student.name,student.phone,status,student.updated.strftime('%X'), student.updated.strftime('%d-%b-%Y')])
        # data += [[ student.name,student.phone, status, student.updated.strftime('%X')]]
    # df = pd.DataFrame(data, columns=['Name','Mobile no','Status','Entry time'])
    # df.to_csv('test.csv')
    mentor = ProfessorDetail.objects.get(user= req.user)
    coursem = mentor.course.course
    print(currentdate)
    students = StudentDetail.objects.filter(course=coursem)
    fileurl =f"media/csv/{currentdate}.csv"
    print(fileurl)
    
    context = {'students':students.order_by('enrollmentno'), 'mentor':mentor,'currentdate':currentdate}
    return render(req,'display.html', context)


@login_required(redirect_field_name='login')
def attendance(req):
    now = datetime.now()
    currentdate =  now.strftime("%d-%b-%Y")
    f =open('media/csv/'+currentdate+'.csv','w+',newline='')
    csvwriter = csv.writer(f)
    csvwriter.writerow(['Roll no', 'Name', 'Mobile no', 'Status','Entry Time','Date'])
    data=[]
    students = StudentDetail.objects.order_by('enrollmentno')
    for student in students:
        status = 'Present' if student.is_present else 'Absent'
        # print(status)
        csvwriter.writerow([student.enrollmentno, student.name,student.phone,status,student.updated.strftime('%X'), student.updated.strftime('%d-%b-%Y')])
        data += [[ student.name,student.phone, status, student.updated.strftime('%X')]]
    
    df = pd.DataFrame(data, columns=['Name','Mobile no','Status','Entry time'])
    df.to_csv('test.csv')
    # df.to_excel(currentdate+'.xlsx')
    # context = {
    #     data : df.to_html()
    # }
    # table =df.to_html(classes=["table"," table-striped ","table-hover"])
    # return HttpResponse()
    context = {'students':students}
    return render(req,'display.html',context)



@login_required(redirect_field_name='login')
def scan(req):
    known_face_encodings = []
    known_face_names = []
    students = StudentDetail.objects.all()
    for student in students:
        image = student.image
        student_face = fc.load_image_file(f'media/{image}')
        face_encoding = fc.face_encodings(student_face)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(student.name)
    
    face_locations = []
    face_encodings = []
    face_names = []
    process=True 
    
    # now = datetime.now()
    # currentdate =  now.strftime("%d-%m-%y")
    # f =open(currentdate+'.csv','w+',newline='')
    # csvwriter = csv.writer(f)
    
    videof = cv2.VideoCapture(0)
    
    while True:
        _,frame = videof.read()
        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_sf = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
        try:
         if process:
            face_locations = fc.face_locations(rgb_sf)
            face_encodings = fc.face_encodings(rgb_sf,face_locations)
            face_names =[]
            for face_encoding in face_encodings:
                matches = fc.compare_faces(known_face_encodings,face_encoding)
                name = ""
                face_distance = fc.face_distance(known_face_encodings, face_encoding)
                best_match = np.argmin(face_distance)
                if matches[best_match]:
                    name = known_face_names[best_match]
                    face_names.append(name)
                student = StudentDetail.objects.get(name=name)
                if student.is_present == True:
                       pass # csvwriter.writerow([student.enrollmentno, student.name, student.updated.strftime])
                else: 
                        student.is_present = True
                        student.save()
        except:
            pass
        process = not process
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 0.5, (255, 255, 255), 1)
            
        cv2.imshow('Attendence System', frame)
        # cv2.putText(frame,'to stop attendence press q', (100,10),fontScale=1)
        if cv2.waitKey(10) == ord('q'):
              break
    
    videof.release()
    cv2.destroyAllWindows()
    # f.close()
    return redirect('display')





