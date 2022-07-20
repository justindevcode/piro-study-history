from multiprocessing import context
from django.shortcuts import render, redirect
from .models import swidea, swtool
import datetime

# Create your views here.

def home(request):
    sort = request.GET.get('sort',None)
    print(sort)
    if sort == '1':
        ideainfo = swidea.objects.all().order_by('ideaname') #__contains는 값이 있으면 가져온다?
    elif sort == '2':
        ideainfo = swidea.objects.all().order_by('ideachoice')
    elif sort == '3':
        ideainfo = swidea.objects.all().order_by()
    elif sort == '4':
        ideainfo = swidea.objects.all().order_by('-id')
    else:
        ideainfo = swidea.objects.all()

    choice = request.GET.get('choice',None)
    if choice != None: 
        choiceidea = swidea.objects.filter(id=choice)
        if choiceidea[0].ideachoice == True:
            swidea.objects.filter(id=choice).update(ideachoice = False)
        else:
            swidea.objects.filter(id=choice).update(ideachoice = True)
    numidplus = request.GET.get('plus',None)
    if numidplus != None:
        a = swidea.objects.filter(id=numidplus)
        b = a[0].ideainterest
        swidea.objects.filter(id=numidplus).update(ideainterest= b+1)
    numidminus = request.GET.get('minus',None)
    if numidminus != None:
        a = swidea.objects.filter(id=numidminus)
        b = a[0].ideainterest
        swidea.objects.filter(id=numidminus).update(ideainterest= b-1)

    context = {
        "ideainfo":ideainfo, 
    }
    return render(request,template_name="swidea/home.html",context=context)

def create(request):
    toollist = swtool.objects.all()
    if request.method == "POST":
        ideaname = request.POST["ideaname"]
        ideaphoto = request.FILES.get("ideaphoto")
        ideacontent = request.POST["ideacontent"]
        ideainterest = request.POST["ideainterest"]
        ideatool = request.POST["ideatool"]
        ideatoolname = swtool.objects.get(id = ideatool)

        swidea.objects.create(ideaname = ideaname, ideaphoto = ideaphoto, ideacontent = ideacontent, ideainterest=ideainterest, ideatool=ideatoolname)
        a = swidea.objects.all()
        return redirect(f"/swidea/{a.last().id}")
    context = {
        "toollist" :toollist
    }
    return render(request, template_name="swidea/create.html", context=context)

def detail(request, id):
    ideainfo = swidea.objects.get(id=id)
    context = {
        "ideainfo": ideainfo,
    }
    return render(request, template_name="swidea/detail.html", context=context)

def update(request, id):
    toollist = swtool.objects.all()
    if request.method == "POST":
        ideaname = request.POST["ideaname"]
        ideaphoto = request.FILES.get("ideaphoto")
        ideacontent = request.POST["ideacontent"]
        ideainterest = request.POST["ideainterest"]
        ideatool = request.POST["ideatool"]
        ideatoolname = swtool.objects.get(id = ideatool)
        # a = request.POST["input_check"]
        # print(a)
        # if a == 1:
        #     swidea.objects.filter(id=id).update(ideaname = ideaname,ideaphoto=ideaphoto,  ideacontent = ideacontent, ideainterest=ideainterest, ideatool=ideatoolname)
        #     return redirect(f"/swidea/{id}")
        # else:
        #     swidea.objects.filter(id=id).update(ideaname = ideaname,  ideacontent = ideacontent, ideainterest=ideainterest, ideatool=ideatoolname)
        #     return redirect(f"/swidea/{id}")
            
        # now = datetime.datetime.now()
        # timepath = now.strftime('/%Y%m%d/')
        # ideaphotopath = 'posts'+timepath+ideaphoto
        swidea.objects.filter(id=id).update(ideaname = ideaname,ideaphoto=ideaphoto,  ideacontent = ideacontent, ideainterest=ideainterest, ideatool=ideatoolname)
        return redirect(f"/swidea/{id}")


    ideainfo = swidea.objects.get(id=id)
    context = {
        "ideainfo": ideainfo,
        "toollist" :toollist,

    }
    return render(request, template_name="swidea/update.html", context=context)

def delete(request,id):
    if request.method == "POST":
        swidea.objects.filter(id=id).delete()
        return redirect("/")


def toolhome(request):
    toolinfo = swtool.objects.all()

    context = {
        "toolinfo":toolinfo, 
    }
    return render(request,template_name="swidea/toolhome.html",context=context)

def tooldetail(request,id):
    toolinfo = swtool.objects.get(id=id)
    ideainfo = swidea.objects.all()
    all_swidea = []
    for i in ideainfo: 
        if toolinfo == i.ideatool:
            all_swidea.append(i)

    context = {
        "toolinfo": toolinfo,
        "all_swidea": all_swidea,
    }
    return render(request, template_name="swidea/tooldetail.html", context=context)


def toolcreate(request):
    if request.method == "POST":
        toolname = request.POST["toolname"]
        tooltype = request.POST["tooltype"]
        toolcontent = request.POST["toolcontent"]

        swtool.objects.create(toolname = toolname, tooltype=tooltype, toolcontent=toolcontent)
        a = swtool.objects.all()
        return redirect(f"/tooldetail/{a.last().id}")
    context = {
    }
    return render(request, template_name="swidea/toolcreate.html", context=context)


def toolupdate(request,id):
    if request.method == "POST":
        toolname = request.POST["toolname"]
        tooltype = request.POST["tooltype"]
        toolcontent = request.POST["toolcontent"]

        swtool.objects.filter(id=id).update(toolname = toolname, tooltype=tooltype, toolcontent=toolcontent)
        return redirect(f"/tooldetail/{id}")

    toolinfo = swtool.objects.get(id = id)
    context = {
        "toolinfo": toolinfo,
    }
    return render(request, template_name="swidea/toolupdate.html", context=context)

def tooldelete(request,id):
    if request.method == "POST":
        swtool.objects.filter(id=id).delete()
        return redirect("/toolhome")