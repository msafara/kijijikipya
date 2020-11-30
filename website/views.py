from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def projects(request):
    return render(request, 'projects.html', {})


def whatwedo(request):
    return render(request, 'whatwedo.html', {})

def contact(request):

    if request.method == "POST":
        nakala = request.POST['nakala']
        majina = request.POST['majina']
        barua = request.POST['barua']
        subject = request.POST['subject']

        return render(request, 'contact.html', {'majina': majina })

        



    else:
        return render(request, 'contact.html', {})
