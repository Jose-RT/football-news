from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406495981',
        'name': 'Jose Ryu Toari',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)