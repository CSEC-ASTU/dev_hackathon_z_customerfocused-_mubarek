from django.shortcuts import render
from blog.models import Blog
from experience.models import Work, Education
from projects.models import Category, Project
from service.models import Service
from skill.models import Skill
from testimonial.models import Testimonials

def home(request):
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
        "blog": blog,
        'category': category,
        'projects': projects,
        'skill1': skill1,
        'skill2': skill2,
        'services': services,
        'education': education,
        'work': work,
        "testimonials": testimonials,
    }
    return render(request, 'index.html', context)