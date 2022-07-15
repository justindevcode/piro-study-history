from django.shortcuts import render, redirect
from .models import Movie, genrebox

# Create your views here.

def home(request):
    
    sort = request.GET.get('sort',7)
    print(sort)
    if sort == '1':
        movieinfo = Movie.objects.all().order_by('title') #__contains는 값이 있으면 가져온다?
    elif sort == '2':
        movieinfo = Movie.objects.all().order_by('-title')
    elif sort == '3':
        movieinfo = Movie.objects.all().order_by('score')
    elif sort == '4':
        movieinfo = Movie.objects.all().order_by('-score')
    elif sort == '5':
        movieinfo = Movie.objects.all().order_by('runningtime')
    elif sort == '6':
        movieinfo = Movie.objects.all().order_by('-runningtime')
    elif sort == '7':
        movieinfo = Movie.objects.all()
    else:
        movieinfo = Movie.objects.all()
        
    

    
    
    context = {
        "movieinfo":movieinfo,
        
        
    }
    return render(request,template_name="movie/home.html",context=context)


def create(request):
    genrename = genrebox.genrele
    print(genrename[0][0])
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        openyear = request.POST["openyear"]
        genre = request.POST["genre"]
        score = request.POST["score"]
        runningtime = request.POST["runningtime"]
        content = request.POST["content"]
        director = request.POST["director"]
        actor = request.POST["actor"]
        Movie.objects.create(title=title,director=director,actor=actor, content=content, openyear=openyear, genre=genre, runningtime=runningtime, score=score)
        return redirect("/") #제출누르면 자동으로 홈으로가서 저장된거보여줌
    context = {
        "genrename":genrename
    }

    return render(request, template_name="movie/create.html", context=context)

def detail(request, id):
    movieinfo = Movie.objects.get(id=id)
    print(movieinfo)
    context = {
        "movieinfo": movieinfo,
        "hour": movieinfo.runningtime//60,
        "min": movieinfo.runningtime %60,
    }
    return render(request, template_name="movie/detail.html", context=context)    

def update(request, id):
    genrename = genrebox.genrele
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        openyear = request.POST["openyear"]
        genre = request.POST["genre"]
        score = request.POST["score"]
        runningtime = request.POST["runningtime"]
        content = request.POST["content"]
        director = request.POST["director"]
        actor = request.POST["actor"]

        
        Movie.objects.filter(id=id).update(title=title,director=director,actor=actor, content=content, openyear=openyear, genre=genre, runningtime=runningtime, score=score)
        return redirect(f"/movie/{id}")


    movieinfo = Movie.objects.get(id=id)
    context = {
        "movieinfo": movieinfo,
        "genrename":genrename
    }
    return render(request, template_name="movie/update.html", context=context)

def delete(request,id):
    if request.method == "POST":
        Movie.objects.filter(id=id).delete()
        return redirect("/")