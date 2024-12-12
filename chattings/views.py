from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CreateTopic,Chats,Department,Replies
from django.shortcuts import get_object_or_404, redirect
from .forms import ChatForm,ReplyForm,TopicForm
from django.db.models import Q

@login_required
def topic_list(request,slug):
    department = get_object_or_404(Department,slug=slug)
    topics = CreateTopic.objects.filter(department=department)
    return render(request, 'topic_home.html', {'department':department,'topics': topics})


@login_required
def start_topic(request,slug):
    department = get_object_or_404(Department, slug=slug)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        slug = request.POST.get('slug')
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.department = department
            topic.save()
            return redirect('topic_list',slug=department.slug)
    else:
        form = TopicForm()
    return render(request,'topic_creation.html',{'form': form,'department':department})

@login_required
def chat_list(request,slug,topic_slug):
    department = get_object_or_404(Department,slug=slug)
    topic = get_object_or_404(CreateTopic, slug=topic_slug, department=department)
    chats = Chats.objects.filter(department=department,topic = topic).order_by('-created_at')
    search_query = request.GET.get('search','')
    print(f"Retrieved chats: {chats}")
    total_images = Chats.objects.filter(department= department,topic=topic).count()
    total_pdfs = Chats.objects.filter(department = department,topic=topic).count()
    if search_query:
        chats = Chats.objects.filter(
            Q(user__username__icontains=search_query) | Q(chats__icontains=search_query),
            department=department,
            topic=topic
        )
    else:
        chats = Chats.objects.filter(department=department, topic=topic).order_by('-created_at')
    
    context = {
        'total_images': total_images,
        'total_pdfs': total_pdfs,
        'chats': chats,
        'department':department,
        'topic':topic,
        'search_query':search_query,

    }
    return render(request,'chatting_list.html',context)

@login_required
def start_chat(request,slug,topic_slug):
    department = get_object_or_404(Department,slug=slug)
    topic = get_object_or_404(CreateTopic, slug=topic_slug, department=department)
    if request.method == 'POST':
        form = ChatForm(request.POST,request.FILES)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.department = department
            chat.topic = topic
            form.save()
            return redirect('chatting_list',slug=department.slug, topic_slug=topic.slug)
    else:
        form = ChatForm()
    return render(request,'chatting_page.html',{'form': form,'department':department,'topic':topic})

@login_required
def edit_chat(request,chat_id,slug,topic_slug):
    chat = get_object_or_404(Chats,pk=chat_id,user = request.user)
    department = get_object_or_404(Department,slug=slug)
    topic = get_object_or_404(CreateTopic,slug=topic_slug,department=department)
    
    if request.method == "POST":
        form = ChatForm(request.POST,instance=chat)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.department = department
            chat.topic = topic
            chat.save()
            return redirect('chatting_list',slug=department.slug, topic_slug = topic.slug)

    else:
        form= ChatForm(instance = chat)
    return render(request,'chat_edit_page.html',{'form':form,'department':department,'topic':topic})





@login_required
def delete_chat(request,chat_id,slug,topic_slug):
    chat = get_object_or_404(Chats,id= chat_id,user = request.user)
    department = get_object_or_404(Department,slug=slug)
    topic = get_object_or_404(CreateTopic,slug=topic_slug,department=department)
    if request.method == "POST":
        chat.department=department
        chat.topic = topic
        chat.delete()
        return redirect('chatting_list', slug=department.slug, topic_slug=topic.slug)
    
    return render(request,'chat_delete.html',{"chat": chat,'department':department,'topic':topic})






@login_required
def reply_chat(request, chat_id,slug,topic_slug):
    
    department = get_object_or_404(Department,slug=slug)
    topic = get_object_or_404(CreateTopic,slug=topic_slug,department=department)
    chat = get_object_or_404(Chats,id=chat_id,department=department, topic=topic)
    form = ReplyForm()
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.chats = chat
            reply.user = request.user
            reply.department = department
            reply.topic = topic
            reply.save()
            return redirect('chatting_list',slug=department.slug, topic_slug = topic.slug)  
    return render(request, 'reply_page.html', {'chat': chat, 'form': form,'department':department,'topic':topic})

@login_required
def replies_list(request, slug, topic_slug, chat_id):
    department = get_object_or_404(Department, slug=slug)
    topic = get_object_or_404(CreateTopic, slug=topic_slug, department=department)
    chat = get_object_or_404(Chats, id=chat_id, department=department, topic=topic)    
    replies = Replies.objects.filter(chats=chat).order_by('replied_at')
    return render(request, 'replies_list.html', {
        'chat': chat,
        'department': department,
        'topic': topic,
        'replies': replies,
    })


@login_required
def imagepage(request,slug,topic_slug,chat_id):
    department = get_object_or_404(Department, slug=slug)
    topic = get_object_or_404(CreateTopic, slug=topic_slug, department=department)
    chat = get_object_or_404(Chats, id=chat_id, department=department, topic=topic)    
    
    return render(request,'chat_image_pdf.html',{'chat':chat,'department':department,'topic':topic})