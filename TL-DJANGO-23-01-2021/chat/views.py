from django.shortcuts import render

from basic.models import User

#Django's inbuilt authentication methods
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Message , connect, myclasses
from chat.serializers import Messageserilizer, Userserializer, Connect, MyClasses

import json
from datetime import date, time, datetime

@csrf_exempt
def user_list(request, pk=None )  :
    if request.method == 'GET' : 
        if pk :
            users = User.objects.filter(id=pk)
        else :
            users = User.objects.all()
        serializer  =  Userserializer(users, many=True , context = {'request' :  request })
        return JsonResponse(serializer.data, safe=False )
    elif request.method == 'POST' : 
        data = JSONParser().parse(request) 
        print("sd")
        serializer = Userserializer(data=data )
        print(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201 )
        return JsonResponse(serializer.errors , status = 400)
@csrf_exempt
def message_list(request, sender=None , receiver = None , viewss=None , idst = None ) :
    if request.method == 'GET' : 
        if viewss  : 

            messages = Message.objects.filter(sender = sender ,  receiver = receiver , id__range = [ idst + 1 , idst + 100000 ]   )  | Message.objects.filter(sender = receiver ,  receiver =  sender, id__range = [ idst + 1 , idst + 100000 ]   )  
            serializer =  Messageserilizer(messages , many=True , context={'request' : request})
            Message.objects.filter(sender =  sender , receiver= receiver ).update(is_read = 1 )
            print(serializer)
            return JsonResponse(serializer.data ,  safe=False )
        else :
            print(sender)
            print(receiver)
            messages = Message.objects.filter(sender = sender ,  receiver = receiver) | Message.objects.filter(sender = receiver , receiver= sender ) 
            Message.objects.filter(sender =  sender , receiver= receiver ).update(is_read = 1 )

            print(messages)
            serializer =  Messageserilizer(messages , many=True , context={'request' : request})
            print(serializer)
 #           Message.objects.filter(sender =  sender , receiver= receiver ).update(is_read = 1 )
            return JsonResponse(serializer.data ,  safe=False )
    elif request.method == 'POST' : 

        data = JSONParser().parse(request) 
        serializer =  Messageserilizer(data = data)
        print(data)


        if viewss is  None :
            sender = int(data['sender'])
            receiver = int(data['receiver'])
            messages = data['message']
            message = Message(message= messages ,  receiver = receiver , sender = sender  )
            message.save()
            serializer = Messageserilizer(message , many=False , context = {'request' : request})
            return JsonResponse(serializer.data , safe = False )
        if serializer.is_valid() :
            print("ok") 
            serializer.save()
            return JsonResponse(serializer.data ,  status=201)
        return JsonResponse(serializer.errors , status=400)
   

def index(request):
    if request.user.is_authenticated: #If the user is authenticated then redirect to the chat console
        return redirect('chats')
    if request.method == 'GET':
        return render(request, 'chat/index.html', {})
    if request.method == "POST": #Authentication of user
        username, password = request.POST['username'], request.POST['password'] #Retrieving username and password from the POST data.
        print(username )
        print(password)
        user = User.objects.filter(username=username, password=password ).exists()

        return redirect('chats')


        if user is not None:
            login(request, User)
        else:
            return HttpResponse('{"error": "User does not exist"}')
        return redirect('chats')


# Simply render the template
def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'chat/register.html', {})

def chat_view(request):
    # Afranzio
    allowed_usr = connect.objects.filter()
    if request.method == "GET":
        return render(request, 'chat/chat.html',
                        {'users': User.objects.exclude(id=request.session['userid'] ), 'sender' : request.session['userid'] , 'receiver' : request.GET.get('receiver')  }) #Returning context for all users except the current logged-in user



#Takes arguments 'sender' and 'receiver' to identify the message list to return
def message_view(request, sender, receiver): 
    """Render the template with required context variables"""
#    if not request.user.is_authenticated:
#        return redirect('index')
    print("DS")
    if request.method == "GET":
        return render(request, "chat/messages.html",
                      {'users': User.objects.exclude(username=request.user.username), #List of users
                       'receiver': User.objects.get(id=receiver), # Receiver context user object for using in template
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)}) # Return context with message objects where users are either sender or receiver.
    if request.method == "POSt" :
        print("ok")  
        
        return  JsonResponse(Status = 200 )

@csrf_exempt 
def makeread(request , sender ,  receiver  ) :
    print("SAD")


# Afranzio

def myclass(request):
    return render(request, 'classes.html')


def api(request):
    usr= myclasses.objects.raw("SELECT * FROM myclasses")
    serializer= MyClasses(usr,many=True)
    return JsonResponse(serializer.data, safe= False)
    # return render(request, 'classes.html', {'se': serializer.data})

def specified(request, sender=None):
    usr= myclasses.objects.raw("SELECT * FROM myclasses Where student_id="+ str(sender) +"")
    serializer= MyClasses(usr,many=True)
    return JsonResponse(serializer.data, safe= False)

def class_form(request):
    return render(request, 'createClass.html')

def create_class(request):
    stu_id = request.session['userid']
    title = request.GET.get("title")
    rate = request.GET.get("rate")
    desc = request.GET.get("desc")
    myclasses.objects.create(student_id = stu_id,teacher_id = "1", class_id=10, class_name = title,class_rate = rate,class_description = desc)
    return render(request, 'classes.html')

# List Tutor
def list_tutor(request):
    tutor_list = User.objects.raw("SELECT * FROM user WHERE role_id = 2")
    serializer= Userserializer(tutor_list,many=True)
    print(serializer.data)
    return render(request, 'listTutor.html', {"se" :serializer.data})

# Invite Tutor
def invite_tutorForm(request):
    return render(request, 'inviteFrom.html')

def invite_tutor(request):
    stu_id = request.session['userid']
    title = request.GET.get('title')
    rate = request.GET.get('rate')
    invitation = connect.objects.create(student_id = stu_id, teacher_id = "12", connect_id=11, class_id = 123, proposal_msg = title, connect_status = rate, connect_teach_rating = 0, connect_rate = rate )
    serializer = Connect(invitation, many=True)
    tutor_list = User.objects.raw("SELECT * FROM user WHERE role_id = 2")
    serializer= Userserializer(tutor_list,many=True)
    return render(request, 'listTutor.html', {"se" :serializer.data})

def myTutors(request):
    stu_id = request.session['userid']
    validate = User.objects.filter(id =  stu_id )
    for i in validate:
        if(i.role_id  == 1):
           return list_tutor(request)
        else:
            tutor_list = connect.objects.raw("SELECT * FROM connect WHERE teacher_id =" +str(stu_id)+ "")
            serializer= Connect(tutor_list,many=True)
            print(serializer.data)
            return render(request, 'listTutor.html', {"invited" :serializer.data})

def show_invitations(request):
    stu_id = request.session['userid']
    tutor_list = connect.objects.raw("SELECT * FROM connect WHERE teacher_id =" +str(stu_id)+ "")
    serializer= Connect(tutor_list,many=True)
    print(serializer.data)
    print(stu_id)
    return render(request, 'listTutor.html', {"invited" :serializer.data})

def approve_tutorForm(request, sender=None):
    stu_id = request.session['userid']
    connect.objects.filter(student_id =  sender , teacher_id= stu_id ).update(connect_status= 1 )
    myclasses.objects.create(class_id = '11', student_id= sender, teacher_id= stu_id)
    return redirect('chats')

