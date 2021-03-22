from django import forms
from RawData.models import  District, School, Position, PositionType


class StaffForm(forms.Form):
    surName = forms.CharField(max_length=500, required=True)
    firstName = forms.CharField(max_length=500, required=True)
    middleName = forms.CharField(max_length=500, required=True)
    extensionName = forms.CharField(max_length=500, required=True)
    dateBirth = forms.DateField(required=True)
    placeBirth = forms.CharField(max_length=500, required=True)
    sex = forms.CharField(max_length=500, required=True)
    civilStatus = forms.CharField(max_length=500, required=True)
    gsisId = forms.CharField(max_length=500, required=True)
    pagibigId = forms.CharField(max_length=500, required=True)
    philhealthId = forms.CharField(max_length=500, required=True)
    tinId = forms.CharField(max_length=500, required=True)
    mobileNum = forms.CharField(max_length=500, required=True)
    depedEmail = forms.CharField(max_length=500, required=True)
    positionType = forms.ModelChoiceField(
        required=True,
        to_field_name="pk",
        queryset=PositionType.objects.all()
    )
    positionName = forms.ModelChoiceField(
        required=True,
        to_field_name="pk",
        queryset=Position.objects.all()
    )
    districtName = forms.ModelChoiceField(
        required=True,
        to_field_name="pk",
        queryset=District.objects.all()
    )
    schoolName = forms.ModelChoiceField(
        required=True,
        to_field_name="pk",
        queryset=School.objects.all()
    )



