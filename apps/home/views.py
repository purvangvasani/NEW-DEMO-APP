# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from .forms import EmployeeForm
from .models import Technology, Questions
from .forms import TechForm, QuestionsForm
from django.shortcuts import render


def index(request):
    technology = Technology.objects.filter(is_active=True)
    context = {
        'segment': 'index',
        'technologies': technology,
        'data_length': len(technology)
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def technologyPage(request, techname):
    tech = Technology.objects.get(techSubname=techname)
    questionArray = Questions.objects.filter(technology_id=tech.id)
    context = {
        'segment': 'technology',
        'params': tech,
        'questionData': questionArray,
        'data_length': len(questionArray),
    }

    if tech.is_active != True:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    html_template = loader.get_template('home/technology.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def viewTechnologyCrud(request):
    technology = Technology.objects.all()
    context = {
        'segment': 'index',
        'technologies': technology,
        'data_length': len(technology)
    }

    html_template = loader.get_template('technology-crud/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def addTechnologyCrud(request):
    context = {'segment': 'index'}
    form = TechForm()
    return render(request, 'technology-crud/add.html', {'form': form})


@login_required(login_url="/login/")
def addTechnologyRecord(request):
    if request.method == "POST":
        form = TechForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse(viewTechnologyCrud))
    else:
        context = {'segment': 'index'}
        html_template = loader.get_template('technology-crud/add.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def editTechnologyRecord(request, id):
    technology = Technology.objects.get(id=id)
    context = {
        'segment': 'technology',
        'technology': technology,
    }

    html_template = loader.get_template('technology-crud/edit.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def editRecord(request, id):
    techName = request.POST['technologyName']
    techSubname = request.POST['technologySubname']
    is_active = request.POST.get('active', False)
    technology = Technology.objects.get(id=id)
    technology.techName = techName
    technology.techSubname = techSubname
    technology.is_active = is_active
    technology.save()
    context = {
        'segment': 'technology',
        'technology': technology,
    }

    html_template = loader.get_template('technology-crud/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def deleteTechnologyRecord(request, id):
    tech = Technology.objects.get(id=id)
    tech.delete()
    return HttpResponseRedirect(reverse(viewTechnologyCrud))


@login_required(login_url="/login/")
def viewQuestionCrud(request):
    questions = Questions.objects.all()
    context = {
        'segment': 'index',
        'questions': questions,
        'data_length': len(questions)
    }

    html_template = loader.get_template('question-crud/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def addQuestionCrud(request):
    context = {'segment': 'index'}
    form = QuestionsForm()
    return render(request, 'question-crud/add.html', {'form': form})


@login_required(login_url="/login/")
def addQuestionRecord(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse(viewQuestionCrud))
    else:
        context = {'segment': 'index'}
        html_template = loader.get_template('question-crud/add.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def editQuestionCrud(request, id):
    question = Questions.objects.get(id=id)
    context = {
        'segment': 'question',
        'question': question,
    }

    html_template = loader.get_template('question-crud/edit.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def editQuestionRecord(request, id):
    techName = request.POST['technologyName']
    techSubname = request.POST['technologySubname']
    is_active = request.POST.get('active', False)
    question = Questions.objects.get(id=id)
    question.techName = techName
    question.techSubname = techSubname
    question.is_active = is_active
    question.save()
    context = {
        'segment': 'question',
        'question': question,
    }

    html_template = loader.get_template('question-crud/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def deleteQuestionRecord(request, id):
    question = Questions.objects.get(id=id)
    question.delete()
    return HttpResponseRedirect(reverse(viewQuestionCrud))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        if load_template == 'index':
            return HttpResponseRedirect(reverse('home:index'))
        # if load_template.split('.')[-1] == 'png':
        #     return render(request, load_template)
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
