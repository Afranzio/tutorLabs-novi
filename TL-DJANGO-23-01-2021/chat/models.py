from django.db import models
from basic.models import User

class Message(models.Model) : 
    sender =models.CharField(max_length= 1200)
    receiver = models.CharField(max_length= 1200)
    message = models.CharField(max_length= 1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read =  models.BooleanField(default=False )
    id = models.AutoField(primary_key=True)
    def __str__(self) : 
        return self.message
    class Meta : 
        ordering  = ('timestamp',) 


class connect(models.Model) : 
    student_id = models.CharField(max_length=40, blank=True ) 
    teacher_id = models.FloatField(max_length=45 , blank=True )
    connect_id = models.CharField(max_length=45 , blank=True )
    class_id = models.AutoField(primary_key=True,null=False)
    connect_status = models.CharField(max_length=60,  blank=True)
    connect_seek_rating = models.CharField(max_length=60,  blank=True, default='0')
    connect_teach_rating = models.CharField(max_length=60,  blank=True)
    connect_rate = models.CharField(max_length=45 , blank=True ,default='0' )
    proposal_msg = models.CharField(max_length=45 , blank=True ,default='New Request from STUDENT' )

    class Meta : 
        managed = False
        db_table = 'connect'

class myclasses(models.Model) : 
    class_id =  models.CharField(primary_key=True, max_length=45,  blank=True )
    student_id = models.CharField(max_length=45, blank=True ) 
    teacher_id = models.FloatField(max_length=45 , blank=True )
    class_name = models.CharField(max_length=45 , blank=True )
    class_rate = models.CharField(max_length=45,  blank=True)
    class_description = models.CharField(max_length=45,  blank=True)

    class Meta : 
        managed = False
        db_table = 'myclasses'

