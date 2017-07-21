from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=120,unique=True)
    pwd= models.CharField(max_length=80)
    age= models.IntegerField()
    sex=models.CharField(max_length=8)
    latitude=models.CharField(max_length=50,default="")
    longitude=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=100,default="")
    blood=models.CharField(max_length=8,default="")
    blood_type=models.CharField(max_length=8,default="")
    phone=models.CharField(max_length=20,default="9508233223")
            
    #no_of_topics=models.IntegerField(default=0)
    #type_user=models.IntegerField(default=0) #simple=0 org=1
    #def __str__(self):
    #    return self

class History(models.Model):
    email = models.CharField(max_length=120,unique=True)
    dis_name = models.CharField(max_length=120)
    dis_severity = models.CharField(max_length=120)
    dis_probname = models.CharField(max_length=120)
    dis_hint = models.CharField(max_length=120)
    dis_time = models.CharField(max_length=120)


"""
class Topic(models.Model):
    #tags = models.ForeignKey(Tag, on_delete = models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    topic_text = models.CharField(max_length=250)
    topic_desc=models.CharField(max_length=700,default="")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.topic_text


class Tag(models.Model):
    tag_name= models.CharField(max_length=50)
    tag_desc=models.CharField(max_length=500,default="")
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    def __str__(self):
        return self.tag_name

class Opinion(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    opinion_text=models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    foragainst=models.IntegerField(default=0) #for=1 against=0
    def __str__(self):
        return self.user.user_name
"""