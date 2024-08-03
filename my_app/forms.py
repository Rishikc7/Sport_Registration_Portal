from django import forms
from my_app.models import VolleyModel, RegistrationModel
from my_app.models import CricketModel
from my_app.models import FootballModel
from my_app.models import BasketballModel
from my_app.models import HockeyModel
from my_app.models import KabaddiModel
from my_app.models import CollegeModel
from my_app.models import BadmintonModel
from my_app.models import TabletennisModel

class VolleyballForm(forms.ModelForm):
    instituteName=forms.CharField(max_length = 200)
    p1=forms.CharField(max_length = 200)
    p2=forms.CharField(max_length = 200)
    p3=forms.CharField(max_length = 200)
    p4=forms.CharField(max_length = 200)
    p5=forms.CharField(max_length = 200)
    p6=forms.CharField(max_length = 200)
    p7=forms.CharField(max_length = 200)
    p8=forms.CharField(max_length = 200)
    p9=forms.CharField(max_length = 200)
    contactNumber=forms.IntegerField(help_text = "Enter 10 digit mobile number")

    class Meta:
        model = VolleyModel
        fields =('instituteName','p1','p2','p3','p4','p5','p6','p7','p8','p9','contactNumber',)
    #     fields=('INSTITUTE_NAME','NAME_OF_PLAYER-1','NAME_OF_PLAYER-2','NAME_OF_PLAYER-3','NAME_OF_PLAYER-4','NAME_OF_PLAYER-5','NAME_OF_PLAYER-6')

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("contactNumber")
        if number>9999999999 or number<6000000000:
            raise forms.ValidationError("Wrong phone number")


class CricketForm(forms.ModelForm):
    instituteName=forms.CharField(max_length = 200)
    p1=forms.CharField(max_length = 200)
    p2=forms.CharField(max_length = 200)
    p3=forms.CharField(max_length = 200)
    p4=forms.CharField(max_length = 200)
    p5=forms.CharField(max_length = 200)
    p6=forms.CharField(max_length = 200)
    p7=forms.CharField(max_length = 200)
    p8=forms.CharField(max_length = 200)
    p9=forms.CharField(max_length = 200)
    p10=forms.CharField(max_length = 200)
    p11=forms.CharField(max_length = 200)
    p12=forms.CharField(max_length = 200)
    p13=forms.CharField(max_length = 200)
    p14=forms.CharField(max_length = 200)
    p15=forms.CharField(max_length = 200)
    contactNumber=forms.IntegerField(help_text = "Enter 10 digit mobile number")

    class Meta:
        model = CricketModel
        fields =('instituteName','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','contactNumber',)

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("contactNumber")
        if number>9999999999 or number<6000000000:
            raise forms.ValidationError("Wrong phone number")


class FootballForm(forms.ModelForm):
    instituteName=forms.CharField(max_length = 200)
    p1=forms.CharField(max_length = 200)
    p2=forms.CharField(max_length = 200)
    p3=forms.CharField(max_length = 200)
    p4=forms.CharField(max_length = 200)
    p5=forms.CharField(max_length = 200)
    p6=forms.CharField(max_length = 200)
    p7=forms.CharField(max_length = 200)
    p8=forms.CharField(max_length = 200)
    p9=forms.CharField(max_length = 200)
    p10=forms.CharField(max_length = 200)
    p11=forms.CharField(max_length = 200)
    p12=forms.CharField(max_length = 200)
    p13=forms.CharField(max_length = 200)
    p14=forms.CharField(max_length = 200)
    p15=forms.CharField(max_length = 200)
    contactNumber=forms.IntegerField(help_text = "Enter 10 digit mobile number")

    class Meta:
        model = FootballModel
        fields =('instituteName','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','contactNumber',)

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("contactNumber")
        if number>9999999999 or number<6000000000:
            raise forms.ValidationError("Wrong phone number")


class BasketballForm(forms.ModelForm):
        instituteName=forms.CharField(max_length = 200)
        p1=forms.CharField(max_length = 200)
        p2=forms.CharField(max_length = 200)
        p3=forms.CharField(max_length = 200)
        p4=forms.CharField(max_length = 200)
        p5=forms.CharField(max_length = 200)
        p6=forms.CharField(max_length = 200)
        p7=forms.CharField(max_length = 200)
        p8=forms.CharField(max_length = 200)
        p9=forms.CharField(max_length = 200)
        contactNumber=forms.IntegerField(help_text = "Enter 10 digit mobile number")

        class Meta:
            model = BasketballModel
            fields =('instituteName','p1','p2','p3','p4','p5','p6','p7','p8','p9','contactNumber',)

        def clean(self):
            cleaned_data = super().clean()
            number = cleaned_data.get("contactNumber")
            if number > 9999999999 or number < 6000000000:
                raise forms.ValidationError("Wrong phone number")


class HockeyForm(forms.ModelForm):
    instituteName=forms.CharField(max_length = 200)
    p1=forms.CharField(max_length = 200)
    p2=forms.CharField(max_length = 200)
    p3=forms.CharField(max_length = 200)
    p4=forms.CharField(max_length = 200)
    p5=forms.CharField(max_length = 200)
    p6=forms.CharField(max_length = 200)
    p7=forms.CharField(max_length = 200)
    p8=forms.CharField(max_length = 200)
    p9=forms.CharField(max_length = 200)
    p10=forms.CharField(max_length = 200)
    p11=forms.CharField(max_length = 200)
    p12=forms.CharField(max_length = 200)
    p13=forms.CharField(max_length = 200)
    p14=forms.CharField(max_length = 200)
    p15=forms.CharField(max_length = 200)
    contactNumber=forms.IntegerField(help_text = "Enter 10 digit mobile number")

    class Meta:
        model = HockeyModel
        fields =('instituteName','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','contactNumber',)

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("contactNumber")
        if number>9999999999 or number<6000000000:
            raise forms.ValidationError("Wrong phone number")



class KabaddiForm(forms.ModelForm):
    instituteName=forms.CharField(max_length = 200)
    p1=forms.CharField(max_length = 200)
    p2=forms.CharField(max_length = 200)
    p3=forms.CharField(max_length = 200)
    p4=forms.CharField(max_length = 200)
    p5=forms.CharField(max_length = 200)
    p6=forms.CharField(max_length = 200)
    p7=forms.CharField(max_length = 200)
    p8=forms.CharField(max_length = 200)
    p9=forms.CharField(max_length = 200)
    p10=forms.CharField(max_length = 200)
    p10=forms.CharField(max_length = 200)
    contactNumber=forms.IntegerField(help_text = "Enter 10 digit mobile number")

    class Meta:
        model = KabaddiModel
        fields =('instituteName','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','contactNumber',)

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("contactNumber")
        if number>9999999999 or number<6000000000:
            raise forms.ValidationError("Wrong phone number")

class Registration(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields =('instituteName','game','date','teams','fee','oneplace','twoplace')

    def clean(self):
        cleaned_data = super().clean()
        teams = cleaned_data.get("teams")
        fee = cleaned_data.get("fee")
        if teams<0 or fee < 0:
            raise forms.ValidationError("Wrong inputs")

class CollegeForm(forms.ModelForm):
    name=forms.CharField(max_length = 200)
    email=forms.EmailField(max_length = 150)
    number=forms.IntegerField(help_text = "Enter 10 digit mobile number")
    festName=forms.CharField(max_length = 200)
    festDesc=forms.CharField(max_length= 2000)
    college=forms.CharField(max_length=200)
    city=forms.CharField(max_length=200)
    state=forms.CharField(max_length=200)
    esd=forms.DateField
    eed=forms.DateField

    class Meta:
        model = CollegeModel
        fields =('name','email','number','festName','festDesc','college','city','state','esd','eed')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("esd")
        end_date = cleaned_data.get("eed")
        number = cleaned_data.get("number")
        if end_date < start_date or number>9999999999 or number<6000000000:
            raise forms.ValidationError("End date should be greater than start date.")

class BadmintonForm(forms.ModelForm):
    instituteName=forms.CharField(max_length = 200,required=False)
    p1 =forms.CharField(max_length = 200,required=False)
    contactNumber = forms.IntegerField(help_text = "Enter 10 digit mobile number",required=False)
    instituteName2 = forms.CharField(max_length = 200,required=False)
    p21 = forms.CharField(max_length = 200,required=False)
    p22 = forms.CharField(max_length = 200,required=False)
    contactNumber2 = forms.IntegerField(help_text = "Enter 10 digit mobile number",required=False)

    class Meta:
        model = BadmintonModel
        fields=('instituteName','p1','contactNumber','instituteName2','p21','p22','contactNumber2')

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("contactNumber")
        number2 = cleaned_data.get("contactNumber2")
        if (number2==None and (number>9999999999 or number<6000000000)) or (number==None and (number2>9999999999 or number2<6000000000)):
            raise forms.ValidationError("Wrong phone number")

class TabletennisForm(forms.ModelForm):
    instituteName=forms.CharField(max_length = 200,required=False)
    p1 =forms.CharField(max_length = 200,required=False)
    contactNumber = forms.IntegerField(help_text = "Enter 10 digit mobile number",required=False)
    instituteName2 = forms.CharField(max_length = 200,required=False)
    p21 = forms.CharField(max_length = 200,required=False)
    p22 = forms.CharField(max_length = 200,required=False)
    contactNumber2 = forms.IntegerField(help_text = "Enter 10 digit mobile number",required=False)

    class Meta:
        model = TabletennisModel
        fields=('instituteName','p1','contactNumber','instituteName2','p21','p22','contactNumber2')

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("contactNumber")
        number2 = cleaned_data.get("contactNumber2")
        if (number2==None and (number>9999999999 or number<6000000000)) or (number==None and (number2>9999999999 or number2<6000000000)):
            raise forms.ValidationError("Wrong phone number")
