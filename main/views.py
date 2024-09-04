from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165843',
        'name': 'Dandi Apriyansyah',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)