from django.urls import path
from.views import list , inprogress , Newprojects , completed , Createproject , UpdateProject, ProjectDetial, DeleteProject

urlpatterns = [
    path("create/", Createproject.as_view(), name="add-new"),
    path("update/<int:pk>/", UpdateProject.as_view(), name="project-update"),
    path("delete/<int:pk>/", DeleteProject.as_view(), name="project-delete"),
    path("detail/<int:pk>/", ProjectDetial.as_view(), name="project-detail"),
    path('' , list , name="list"),
    path('progress/' , inprogress),
    path('new/' , Newprojects),
    path('completed/' , completed)

]
