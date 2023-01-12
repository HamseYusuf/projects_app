from django.shortcuts import render , reverse , redirect
from.models import Project
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from.forms import ProjectsForm ,  UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages





def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/singup.html', {'form': form})


   
   




class Createproject(LoginRequiredMixin,generic.CreateView):
    queryset = Project.objects.all()
    template_name = 'projects/create.html'
    fields = ['title' , 'category' , 'technology' , 'developers' , 'details' , 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

    def get_success_url(self) :
        return reverse('list')

class UpdateProject(LoginRequiredMixin,generic.UpdateView):
    queryset = Project.objects.all()
    template_name = 'projects/update.html'
    fields = ['title' , 'category' , 'technology' , 'developers' , 'details' , 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

    def get_success_url(self) :
        return reverse('list')

class ProjectDetial(generic.DeleteView):
    model = Project
    template_name = 'projects/detail.html'
    context_object_name = 'project'

class DeleteProject(LoginRequiredMixin,generic.DeleteView):
    model = Project
    template_name = 'projects/delete.html'
    context_object_name = 'project'

    def get_success_url(self) :
        return reverse('list')


def list(request):
    projects = Project.objects.all().order_by('-id')
    context = {
        'projects': projects
    }
    return render(request , 'projects/list.html', context)

def inprogress(request):
    projects = Project.objects.filter(status= 'inprogress')
    context = {
        'projects': projects
    }
    return render(request , 'projects/inprogress.html' ,context)

def Newprojects(request):
    projects = Project.objects.filter(status= 'new').order_by('-id')
    context = {
        'projects': projects
    }
    return render(request , 'projects/Newprojects.html' ,context)

def completed(request):
    projects = Project.objects.filter(status= 'completed')
    context = {
        'projects': projects
    }
    return render(request , 'projects/completed.html' ,context)