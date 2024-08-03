from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CollegeModel(models.Model):
    name=models.CharField(max_length = 200)
    email=models.EmailField(max_length = 150)
    number=models.IntegerField(help_text = "Enter 10 digit mobile number")
    festName=models.CharField(max_length = 200, unique=True)
    festDesc=models.CharField(max_length= 2000)
    college=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    esd=models.DateField(null=True)
    eed=models.DateField(null=True)
    created_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.festName


class RegistrationModel(models.Model):
    instituteName = models.CharField(max_length=200)
    game = models.CharField(max_length=200)
    date = models.DateField(null=True)
    teams = models.IntegerField(null=True)
    fee = models.IntegerField(null=True)
    oneplace = models.CharField(max_length=200)
    twoplace = models.CharField(max_length=200)
    fest = models.ForeignKey(CollegeModel, null=True, to_field='festName',  on_delete=models.CASCADE)

    def __str__(self):
        return self.instituteName + "_" + self.game



class VolleyModel(models.Model):
        venue=models.CharField(max_length = 200,default='',null=True)
        instituteName=models.CharField(max_length = 200)
        p1=models.CharField(max_length = 200)
        p2=models.CharField(max_length = 200)
        p3=models.CharField(max_length = 200)
        p4=models.CharField(max_length = 200)
        p5=models.CharField(max_length = 200)
        p6=models.CharField(max_length = 200)
        p7=models.CharField(max_length = 200)
        p8=models.CharField(max_length = 200)
        p9=models.CharField(max_length = 200)
        contactNumber=models.IntegerField(help_text = "Enter 10 digit mobile number")
        inst = models.ForeignKey(RegistrationModel, null=True, on_delete=models.CASCADE)

        def __str__(self):
            return self.instituteName + "_" + str(self.contactNumber)


class CricketModel(models.Model):
    venue=models.CharField(max_length = 200,default='',null=True)
    instituteName=models.CharField(max_length = 200)
    p1=models.CharField(max_length = 200)
    p2=models.CharField(max_length = 200)
    p3=models.CharField(max_length = 200)
    p4=models.CharField(max_length = 200)
    p5=models.CharField(max_length = 200)
    p6=models.CharField(max_length = 200)
    p7=models.CharField(max_length = 200)
    p8=models.CharField(max_length = 200)
    p9=models.CharField(max_length = 200)
    p10=models.CharField(max_length = 200)
    p11=models.CharField(max_length = 200)
    p12=models.CharField(max_length = 200)
    p13=models.CharField(max_length = 200)
    p14=models.CharField(max_length = 200)
    p15=models.CharField(max_length = 200)
    contactNumber=models.IntegerField(help_text = "Enter 10 digit mobile number")
    inst = models.ForeignKey(RegistrationModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.instituteName + "_" + str(self.contactNumber)



class FootballModel(models.Model):
    venue=models.CharField(max_length = 200,default='',null=True)
    instituteName=models.CharField(max_length = 200)
    p1=models.CharField(max_length = 200)
    p2=models.CharField(max_length = 200)
    p3=models.CharField(max_length = 200)
    p4=models.CharField(max_length = 200)
    p5=models.CharField(max_length = 200)
    p6=models.CharField(max_length = 200)
    p7=models.CharField(max_length = 200)
    p8=models.CharField(max_length = 200)
    p9=models.CharField(max_length = 200)
    p10=models.CharField(max_length = 200)
    p11=models.CharField(max_length = 200)
    p12=models.CharField(max_length = 200)
    p13=models.CharField(max_length = 200)
    p14=models.CharField(max_length = 200)
    p15=models.CharField(max_length = 200)
    contactNumber=models.IntegerField(help_text = "Enter 10 digit mobile number")
    inst = models.ForeignKey(RegistrationModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.instituteName + "_" + str(self.contactNumber)


class BasketballModel(models.Model):
    venue=models.CharField(max_length = 200,default='',null=True)
    instituteName=models.CharField(max_length = 200)
    p1=models.CharField(max_length = 200)
    p2=models.CharField(max_length = 200)
    p3=models.CharField(max_length = 200)
    p4=models.CharField(max_length = 200)
    p5=models.CharField(max_length = 200)
    p6=models.CharField(max_length = 200)
    p7=models.CharField(max_length = 200)
    p8=models.CharField(max_length = 200)
    p9=models.CharField(max_length = 200)
    contactNumber=models.IntegerField(help_text = "Enter 10 digit mobile number")
    inst = models.ForeignKey(RegistrationModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.instituteName + "_" + str(self.contactNumber)

class HockeyModel(models.Model):
        venue=models.CharField(max_length = 200,default='',null=True)
        instituteName=models.CharField(max_length = 200)
        p1=models.CharField(max_length = 200)
        p2=models.CharField(max_length = 200)
        p3=models.CharField(max_length = 200)
        p4=models.CharField(max_length = 200)
        p5=models.CharField(max_length = 200)
        p6=models.CharField(max_length = 200)
        p7=models.CharField(max_length = 200)
        p8=models.CharField(max_length = 200)
        p9=models.CharField(max_length = 200)
        p10=models.CharField(max_length = 200)
        p11=models.CharField(max_length = 200)
        p12=models.CharField(max_length = 200)
        p13=models.CharField(max_length = 200)
        p14=models.CharField(max_length = 200)
        p15=models.CharField(max_length = 200)
        contactNumber=models.IntegerField(help_text = "Enter 10 digit mobile number")
        inst = models.ForeignKey(RegistrationModel, null=True, on_delete=models.CASCADE)

        def __str__(self):
            return self.instituteName + "_" + str(self.contactNumber)


class KabaddiModel(models.Model):
        venue=models.CharField(max_length = 200,default='',null=True)
        instituteName=models.CharField(max_length = 200)
        p1=models.CharField(max_length = 200)
        p2=models.CharField(max_length = 200)
        p3=models.CharField(max_length = 200)
        p4=models.CharField(max_length = 200)
        p5=models.CharField(max_length = 200)
        p6=models.CharField(max_length = 200)
        p7=models.CharField(max_length = 200)
        p8=models.CharField(max_length = 200)
        p9=models.CharField(max_length = 200)
        p10=models.CharField(max_length = 200)
        p11=models.CharField(max_length = 200)
        contactNumber=models.IntegerField(help_text = "Enter 10 digit mobile number")
        inst = models.ForeignKey(RegistrationModel, null=True, on_delete=models.CASCADE)

        def __str__(self):
            return self.instituteName + "_" + str(self.contactNumber)


class BadmintonModel(models.Model):
    venue=models.CharField(max_length = 200,default='',null=True)
    instituteName=models.CharField(max_length = 200,default='',null=True)
    p1 =models.CharField(max_length = 200,default='',null=True)
    contactNumber = models.IntegerField(help_text = "Enter 10 digit mobile number",default='',null=True)
    instituteName2 = models.CharField(max_length = 200,default='',null=True)
    p21 = models.CharField(max_length = 200,default='',null=True)
    p22 = models.CharField(max_length = 200,default='',null=True)
    contactNumber2 = models.IntegerField(help_text = "Enter 10 digit mobile number",default='',null=True)
    inst = models.ForeignKey(RegistrationModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.contactNumber2==None or self.contactNumber2=='':
            return self.instituteName + "_" + str(self.contactNumber)
        elif self.contactNumber==None or self.contactNumber=='':
            return self.instituteName + "_" + str(self.contactNumber2)

class TabletennisModel(models.Model):
    venue=models.CharField(max_length = 200,default='',null=True)
    instituteName=models.CharField(max_length = 200,default='',null=True)
    p1 =models.CharField(max_length = 200,default='',null=True)
    contactNumber = models.IntegerField(help_text = "Enter 10 digit mobile number",default='',null=True)
    instituteName2 = models.CharField(max_length = 200,default='',null=True)
    p21 = models.CharField(max_length = 200,default='',null=True)
    p22 = models.CharField(max_length = 200,default='',null=True)
    contactNumber2 = models.IntegerField(help_text = "Enter 10 digit mobile number",default='',null=True)
    inst = models.ForeignKey(RegistrationModel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.contactNumber2==None or self.contactNumber2=='':
            return self.instituteName + "_" + str(self.contactNumber)
        elif self.contactNumber==None or self.contactNumber=='':
            return self.instituteName + "_" + str(self.contactNumber2)
