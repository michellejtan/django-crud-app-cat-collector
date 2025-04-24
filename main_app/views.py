from django.shortcuts import render, redirect   # already here, to render something #let's insert something control logic
# from django.http import HttpResponse #close to: express res.send
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
from .forms import FeedingForm

# Create your views here.

# controller code in python
# we call these view functions
def home(request):
    # each view function or "view"
    # recevices a request object
    # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    #refactor
    return render(request, 'home.html')
    # to send a response, we return it!

def about(request):
     contact_details = 'you can reach support at support@catcollector.com' 
     return render(request, 'about.html', {
        'contact': contact_details
    }) # this is the same as res.render()

# views.py

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]


def cat_index(request):
    # Render the cats/index.html template with the cats data
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
     # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        # include the cat and feeding_form in the context
        'cat': cat,
        'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        # ^ save in memory, but do NOT commit to the db
        new_feeding.cat_id = cat_id 
        #making the association to the cat
        new_feeding.save() # now it's saved to the database
    return redirect('cat-detail', cat_id=cat_id) # like render we need to import it
    # does do reverse method, provide as second argument 

class CatCreate(CreateView):
    model = Cat
    # fields = '__all__'  # like a lazy method
    fields = ['name', 'breed', 'description', 'age']
    # Remove success_url so Django uses get_absolute_url from Cat
    # success_url = '/cats'

class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'