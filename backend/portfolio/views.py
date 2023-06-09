from django.http import HttpResponse
from django.http import FileResponse
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404, render
import requests
from about.models import About
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
from cv.models import Cv

# from . import scrapped
def scrap(m,n,o,r,s,k=0,w=0,p=0,q=0):
    url = m
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    score_element = soup.find_all(n, class_=o)[k]
    if p and q:
        rank_element = soup.find_all(p, class_=q)[w]
    else:
        rank_element = None

    score = score_element.text.strip() if score_element else "N/A"
    rank = rank_element.text.strip() if rank_element else ""

    absolute_logo_url = f"../../media/scrape/{s}"

    name = r
    return name, absolute_logo_url,score, rank

cses = scrap("https://cses.fi/user/119282","td","", "CSES", "cses.png")
codeforces = scrap("https://codeforces.com/profile/mukeremali","div","_UserActivityFrame_counterValue", "Codeforces", "codeforces.png")
kattis = scrap("https://open.kattis.com/users/mukerem", "span", "important_number", "Kattis", "kattis.png",1,0, "span", "important_number")
HallOfFame = scrap("https://cphof.org/profile/codeforces:mukeremali", "td", "light-cell", "Hall of Fame", "halloffame.png", -1,0, "td", "light-cell")
leetcode = scrap("https://leetcode.com/mukeremali112/", "div", "text-[24px] font-medium text-label-1 dark:text-dark-label-1", "Leetcode", "halloffame.png", p="span", q="ttext-label-1 dark:text-dark-label-1 font-medium")
def scraped():
    data=[]
    d=[cses, codeforces, HallOfFame, kattis, leetcode]
    for i in d:
        e,a,b,c = i
        f={
            'name': e,
            'link': a,
            'score':b,
            'rank': c,
        }
        data.append(f)
    
    return data


def home(request):
    scrap = scraped()
    profile = Profile.objects.get(id=1)
    cv = Cv.objects.get(profile=profile)
    social = SocialAccount.objects.filter(profile=profile)
    comp = Competitions.objects.all()
    training = Trainings.objects.all()
    about = About.objects.get(profile=profile)
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
        'cv': cv,
        'scrap': scrap,
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
        'about': about,
    }
    return render(request, 'index.html', context)


def download_pdf(request, document_id):
    document = Cv.objects.get(id=document_id)
    file_path = document.cv.path
    response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="document.pdf"'
    return response