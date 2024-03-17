from django.shortcuts import render
from datetime import datetime

# Create your views here.

def addition():
    i = 0 
    while i < 100:
        i += 1

def home(request):
    dynamic_data = {
        "students":{
          'st_name':['AB','AC','AD','AF'],
          'roll_no':[1,2,3,4],
          'address':['is','fsd','lah','kara']  
        },
        "course_name":"Django",
        "course_duration": 4,
        "total_seats":40,
        "p": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam assumenda ea recusandae nostrum alias iusto, consequuntur maiores iste facilis hic rem nihil, nobis unde tempore eveniet ad. Modi, architecto ex.",
        "date_value":"2024-08-01",
        'd':datetime.now(),
        'a':232.222,
        'b':232.222,
        'c':232.222,
        'nm':"abdullah",
        'it':addition()
    }
    
    stu = {
        'st1':{"name":"Omer","roll":20},
        'st2':{"name":"Hamza","roll":30},
        'st3':{"name":"Talha","roll":40},
    }
    st = {'students':stu}
    return render(request, 'IS/index.html',context=st)

