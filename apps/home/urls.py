# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('technology/<techname>', views.technologyPage, name='technology'),

    # Technology CRUD
    path('technology-crud/view', views.viewTechnologyCrud, name='technologycrud'),
    path('technology-crud/add', views.addTechnologyCrud, name='technologyadd'),
    path('technology-crud/add/addrecord/',
         views.addTechnologyRecord, name="technologyaddrecord"),
    path('technology-crud/edit/<int:id>',
         views.editTechnologyRecord, name="technologyedit"),
    path('technology-crud/edit/updaterecord/<int:id>',
         views.editRecord, name='technologyeditrecord'),
    path('technology-crud/remove/<int:id>',
         views.deleteTechnologyRecord, name='technologydelete'),

    # Questions CRUD
    path('questions/view', views.viewQuestionCrud, name='questionscrud'),
    path('questions/add', views.addQuestionCrud, name='questionsadd'),
    path('questions/add/addrecord/',
         views.addQuestionRecord, name="questionsaddrecord"),
    path('questions/edit/<int:id>',
         views.editQuestionCrud, name="questionsedit"),
    path('questions/edit/updaterecord/<int:id>',
         views.editQuestionRecord, name='questionseditrecord'),
    path('questions/remove/<int:id>',
         views.deleteQuestionRecord, name='questionsdelete'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
