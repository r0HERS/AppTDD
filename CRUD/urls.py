from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add",views.add,name="add"),
    path("del/<str:m_id>",views.dele,name="del"),
    path("search",views.search,name="search"),
    path("edit/<str:c_id>",views.edit,name="edit"),
    path("att/<str:c_id>",views.edit,name="atualiza"),

    #rota alunos

    path("add_al",views.add_al,name="add_al")
]
