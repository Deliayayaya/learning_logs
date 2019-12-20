from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse,Http404
from . import models
from .form import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required

def err404(model,request):
    if model.owner != request.user:
        raise Http404

def index(request):
    return render(request,'learn/index.html')

@login_required
def topics(request):
    print("re==",request.user)
    topics = models.Topic.objects.filter(owner = request.user).order_by('-time_added')
    return render(request,'learn/topics.html',{'topics':topics})

@login_required
def topic(request,topic_id):
    topic = models.Topic.objects.get(id=topic_id)
    err404(topic,request)
    # if topic.owner != request.user:
    #     raise Http404
    entries = topic.entry_set.order_by('-date_added')
    content = {'topic':topic,'entries':entries}
    return render(request,'learn/topic.html',content)

@login_required
def new_topic(request):
    if request.method !='POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learn:topics'))
    content ={'form':form}
    return render(request,'learn/new_topic.html',content)

@login_required
def new_entry(request,topic_id):
    topic = models.Topic.objects.get(id=topic_id)
    #添加一个新的条目
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('learn:topic',args=[topic_id]))
    content = {'form':form,'topic':topic}
    print(content)

    return render(request,'learn/new_entry.html',content)

@login_required
def edit_entry(request,entry_id):
    entry = models.Entry.objects.get(id=entry_id)
    topic = entry.topic
    err404(topic,request)
    if request.method !='POST':
         form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learn:topic',args=[topic.id]))
    content ={'entry':entry,'topic':topic,'form':form}
    print("content111",content)
    return render(request,'learn/edit_entry.html',content)