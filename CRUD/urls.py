from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add",views.add,name="add"),
    path("del/<str:m_id>",views.dele,name="del"),
    path("att/<str:c_id>",views.edit_curso,name="atualiza"),

    # ROTA ALUNOS
    path("search/<str:al_id>",views.search,name="search"),
    path("add_al",views.add_al,name="add_al"),
    path("del_al/<str:a_id>",views.del_al,name="del_al"),
    path("edit_al/<str:al_id>",views.edit_al,name="edit_al"),

    # ROTA CURSOS
    path("edit/<str:c_id>",views.edit_curso,name="edit"),
    path("search_curso",views.search_curso,name="search_curso"),
    path("add_curso",views.add_curso,name="add_curso"),
    path("del_curso/<str:c_id>",views.del_curso,name="del_curso"),

    #ROTA MATÉRIAS

    path("add_materia",views.add_mat,name="add_materia"),
    path("search_materia",views.search_materia,name="search_materia"),
    path("edit_materia/<str:mat_id>",views.edit_materia,name="edit_materia"),

    # ROTA PROFESSORES
    path("cria_prof",views.add,name="cria_prof"),
    path("del_prof/<str:prof_id>",views.del_prof,name="del_prof"),
    path("edit_prof/<str:prof_id>",views.edit_prof,name="edit_prof"),

    path("search_prof",views.search_prof,name="search_prof")
]
