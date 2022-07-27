from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comment

# Create your views here.

def home(request):
    commentinfo = Comment.objects.all()
    context={
        "commentinfo": commentinfo,
    }

    return render(request, "pirostagram/home.html", context=context)

@csrf_exempt
def content_ajax(request):
    req = json.loads(request.body)
    comment_content = req['content']
    Comment.objects.create(content = comment_content)
    findid = Comment.objects.last()
    idnum = findid.id

    return JsonResponse({'content': comment_content,'id': idnum})


@csrf_exempt
def like_ajax(request):
    print(6)
    req = json.loads(request.body)
    comment_id = req['id']
    button_type = req['type']

    commentid = Comment.objects.get(id = comment_id)
    if button_type == 'like':
        commentid.like = False
        button_type = 'dislike'

    else:
        commentid.like = True
        button_type = 'like'
    commentid.save()

    return JsonResponse({'id': comment_id, 'type': button_type})

@csrf_exempt
def delete_ajax(request):
    req = json.loads(request.body)
    comment_id = req['id']
    Comment.objects.filter(id=comment_id).delete()
    return JsonResponse({'id': comment_id})


