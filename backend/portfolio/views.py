from django.shortcuts import render
from blog.models import Blog
from experience.models import Work, Education
from projects.models import Category, Project
from service.models import Service
from skill.models import Skill
from testimonial.models import Testimonials
from tutorial.models import Tutorial
from competitions.models import Competitions
from profiles.models import Profile, SocialAccount
from trainings.models import Trainings

def home(request):
    profile = Profile.objects.get(id=1)
    social = SocialAccount.objects.filter(profile=profile)
    comp = Competitions.objects.all()
    training = Trainings.objects.all()
    try:
        comp1 = comp[:len(comp)//2]
        comp2 = comp[len(comp)//2:]
        train1 = training[:len(training)//2]
        train2 = training[len(training)//2:]
    except:
        comp1=''
        comp2=''
    tutorial = Tutorial.objects.all()
    tutorial1 = tutorial[:len(tutorial)//2]
    tutorial2 = tutorial[len(tutorial)//2:]
    blog = Blog.objects.all()
    category = Category.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    skill = Skill.objects.all()
    skill1 = skill[:len(skill)//2]
    skill2 = skill[len(skill)//2::]
    work = Work.objects.all()
    testimonials = Testimonials.objects.all()
    context = {
        'train1': train1,
        'train2': train2,
        'profile': profile,
        'social': social,
        "blog": blog,
        'category': category,
        'projects': projects,
        'skill1': skill1,
        'skill2': skill2,
        'services': services,
        'education': education,
        'work': work,
        "testimonials": testimonials,
        'tutorial1': tutorial1,
        'tutorial2': tutorial2,
        'comp1': comp1,
        'comp2': comp2,
    }
    return render(request, 'index.html', context)