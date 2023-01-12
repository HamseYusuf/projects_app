from django.urls import path
from.views import list , inprogress , Newprojects , completed , Createproject , UpdateProject, ProjectDetial, DeleteProject ,  register

urlpatterns = [
    path("singup/",register, name="singup"),
    path("create/", Createproject.as_view(), name="project-create"),
    path("update/<int:pk>/", UpdateProject.as_view(), name="project-update"),
    path("delete/<int:pk>/", DeleteProject.as_view(), name="project-delete"),
    path("detail/<int:pk>/", ProjectDetial.as_view(), name="project-detail"),
    path('projects/' , list , name="list"),
    path('progress/' , inprogress , name ="project-progress"),
    path('' , Newprojects , name ="project-new-projects"),
    path('completed/' , completed ,  name="project-completed")

]
