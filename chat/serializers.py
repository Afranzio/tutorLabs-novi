from basic.models import User
from rest_framework import serializers 
from chat.models import Message , connect, myclasses

# start the serializer


class Userserializer(serializers.ModelSerializer) :
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User 
        fields = ['username' , 'password' , 'email_id' , 'role'] 

class Messageserilizer(serializers.ModelSerializer) :
      class Meta : 
        model = Message 
        fields = ['sender', 'receiver' , 'message' , 'timestamp' , 'id']

class Connect(serializers.ModelSerializer) :
      class Meta : 
        model = connect 
        fields = ['student_id','teacher_id','connect_id','class_id','connect_status','connect_seek_rating','connect_teach_rating','connect_rate', 'proposal_msg']

class MyClasses(serializers.ModelSerializer) :
      class Meta : 
        model = myclasses 
        fields = ['student_id','teacher_id','class_name','class_rate','class_description']