from django.shortcuts import render, HttpResponseRedirect
from .forms import Include
from .models import User
# Create your views here.

#Add and Show Items
def adshow(request):
    if request.method == 'POST':
        inc = Include(request.POST)
        if inc.is_valid():
            celebrity=inc.cleaned_data['celebrity']
            movie=inc.cleaned_data['movie']
            imdb=inc.cleaned_data['imdb']
            us=User(celebrity=celebrity, movie=movie, imdb=imdb)
            us.save()
            inc=Include()
    else:
        inc = Include()
    stud = User.objects.all()
    return render(request, 'enroll/adshow.html', {'ind':inc, 'stu':stud})

#Update Items
def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        inc=Include(request.POST, instance=pi)
        if inc.is_valid():
            inc.save()
    else:
        pi = User.objects.get(pk=id)
        inc = Include(instance=pi)
    return render(request, 'enroll/update.html', {'ind':inc})


#Delete Items
def delete(request, id):
    if request.method == 'POST':
      pi = User.objects.get(pk=id)
      pi.delete()
    return HttpResponseRedirect('/')  
