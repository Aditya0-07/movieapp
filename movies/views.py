from django.shortcuts import render
from django.urls import reverse_lazy
from movies.models import Movies
from movies.forms import movieform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

# def home(request):
#     m = Movies.objects.all()
#     return render(request,'home.html',{'m':m})

class HomeView(ListView):
    model = Movies
    template_name = "home.html"
    context_object_name = 'm'


# def details(request,n):
#     d = Movies.objects.get(id=n)
#     return render(request,'detailspage.html',{'details':d})

class Detail(DetailView):
    model = Movies
    template_name = "detailspage.html"
    context_object_name = 'details'

# def add(request):
#     if (request.method == "POST"):    #  after form submission ,This conditional checks if the request method is POST, meaning that the form has been submitted.
#         form = movieform(request.POST, request.FILES)  # In Django, when handling forms that include file uploads (like images), you need to include request.FILES along with request.POST in the form instantiation to access the uploaded files.
#                                                       # This line creates an instance of the movieform form class with the data submitted via POST, including the files.
#         if form.is_valid():  # checks validity of the form, is_valid():
#             form.save()
#             return home(request)                        # After successfully saving the form data, this line redirects the user to the home page.
#
#     form = movieform()                 #If the request method is not POST, this line creates a new instance of the movieform form class without any data. This is used to display the empty form to the user initially.
#
#     return render(request,'addmovie.html',{'form':form})

class AddMovie(CreateView):
    model = Movies
    template_name = "addmovie.html"
    fields = ['name', 'year', 'desc', 'image']
    success_url = reverse_lazy('movies:home')


# def edit(request,n):
#     ed = Movies.objects.get(id=n)  # to get the particular element with id
#     if (request.method == "POST"):
#
#         form1 = movieform(request.POST, request.FILES,instance=ed)  # Here, a form instance (form1) is created using the data from the POST request (request.POST) and any files uploaded (request.FILES).
#                                                                     # The instance=ed parameter specifies that the form is bound to the ed movie object retrieved earlier, allowing the form to prepopulate fields with existing data for editing.
#         if form1.is_valid():
#             form1.save()
#             return details(request,n)              #After saving the changes, the view redirects the user to the movie details page for the edited movie (details view), passing the same movie ID (n).
#
#     form1 = movieform(instance=ed)  # instance = ed, to get the datas already when editing. when initially the page loads w want the form together with the data.
#     return render(request, 'editpage.html', {'form': form1})

class Update(UpdateView):
    model = Movies
    template_name = "addmovie.html"
    fields = ['name', 'year', 'desc', 'image']
    success_url = reverse_lazy('movies:home')

# def delete(request,n):
#     de = Movies.objects.get(id=n)
#     de.delete()
#     return reverse_lazy('app : home')

class Delete(DeleteView):
    model = Movies
    template_name = "delete.html"
    success_url = reverse_lazy('movies:home')


