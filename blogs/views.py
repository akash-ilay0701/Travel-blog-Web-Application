from django.shortcuts import render
from .models import TravelBlog
from django.views.generic import CreateView
from .forms import BlogForm
# Create your views here.

def home(request):
    blog = TravelBlog.objects.all()
    return render(request, "home.html", {'blogs': blog})



#
# def createdBlog(request):
#     cdblog = TravelBlog()
#     cdblog.title = request.POST.get("title")
#     #cdblog.nameOfAuthor = request.POST.get("author")
#     cdblog.date = request.POST.get("date")
#     cdblog.description = request.POST.get("description")
#     cdblog.thumbnail = request.POST.get("thumbnail")
#     cdblog.save()
#     return redirect('confirmed')

def confirmed(request):
    return render(request, "confirmed.html")


def seeMore(request, pk):
    blog = TravelBlog.objects.get(pk=pk)
    return render(request, "seeMore.html", {'blog': blog})

# def profile(request):
#     return render(request, "")

class AddBlog(CreateView):
    form_class = BlogForm
    model = TravelBlog
    template_name = "addBlog.html"
    success_url = '/confirmed'
