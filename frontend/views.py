from django.shortcuts import render, HttpResponse
from .models import Project, ProjectInMind, Contact, Category


# Create your views here.
def HomeView(request):
    # project = Project.objects.all().order_by('?')[:3]
    projects = Project.objects.all().order_by('-date_posted')
    project_in_mind = ProjectInMind.objects.all().order_by('-date_posted')[:1]

    if request.method == 'POST':
        contact = Contact()
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        # return HttpResponse('<h1>Thanks for contacting us, sfcode will replay as soon as possible</h1>')
        return render(request, 'frontend/thank_you.html')
    context = {
        'projects': projects,
        'project_in_mind': project_in_mind,
    }
    return render(request, 'frontend/homePage.html', context)



def ProjectDetailedView(request, slug):
    project = Project.objects.get(slug=slug)

    context = {
        'project': project,
    }
    return render(request, 'frontend/single-project.html', context)



def CategoryView(request, slug):
    category = Category.objects.get(slug=slug)

    context = {
        'category': category,
    }
    return render(request, 'frontend/project-category.html', context)



