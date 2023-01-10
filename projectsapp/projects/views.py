from django.shortcuts import render , reverse
from.models import Project
from django.views import generic
from.forms import ProjectsForm



class Createproject(generic.CreateView):
    queryset = Project.objects.all()
    template_name = 'projects/create.html'
    fields = ['title' , 'category' , 'technology' , 'developers' , 'details' , 'status']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

    def get_success_url(self) :
        return reverse('list')

class UpdateProject(generic.UpdateView):
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

class DeleteProject(generic.DeleteView):
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
    inporgress = Project.objects.filter(status= 'inprogress')
    context = {
        'projects': inporgress
    }
    return render(request , 'projects/inprogress.html' ,context)

def Newprojects(request):
    inporgress = Project.objects.filter(status= 'new')
    context = {
        'projects': inporgress
    }
    return render(request , 'projects/Newprojects.html' ,context)

def completed(request):
    inporgress = Project.objects.filter(status= 'completed')
    context = {
        'projects': inporgress
    }
    return render(request , 'projects/completed.html' ,context)