from django.shortcuts import render

# Create your views here.
def home(request):
    dynamic_data = {
        "course_name":"Django",
        "course_duration": 4,
        "total_seats":40,
        "p": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam assumenda ea recusandae nostrum alias iusto, consequuntur maiores iste facilis hic rem nihil, nobis unde tempore eveniet ad. Modi, architecto ex.",
        "date_value":"2024-08-01"
    }
    return render(request, 'IS/index.html',context=dynamic_data)
