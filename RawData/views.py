from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .import views
from .models import StaffData, District, School, Position, PositionType
from .forms import StaffForm
import pdb


def index(request):
    district = District.objects.all()
    school = School.objects.all()
    positionType = PositionType.objects.all()
    context = {
        'district': district,
        'school': school,
        'positionType': positionType

    }
    return render(request, 'index.html', context)


def school_request(request):

    if request.method == 'POST':
        district_id = request.POST.get('id', None)
        school = School.objects.filter(districtName=district_id).values("id", "schoolName")
        return JsonResponse({"data": list(school)})
    else:
        return HttpResponse()


def position_request(request):
    if request.method == 'POST':
        positiontype_id = request.POST.get('id', None)
        position = Position.objects.filter(positionType=positiontype_id).values("id", "positionName")
        return JsonResponse({"data": list(position)})
    else:
        return HttpResponse()


def addstaff_request(request):
    if request.method == 'POST':
        form = StaffForm(data=request.POST)

        if form.is_valid():
            datas = form.cleaned_data
            StaffData.objects.create(
                surName =datas['surName'],
                firstName =datas['firstName'],
                middleName =datas['middleName'],
                extensionName =datas['extensionName'],
                dateBirth =datas['dateBirth'],
                placeBirth =datas['placeBirth'],
                sex =datas['sex'],
                civilStatus =datas['civilStatus'],
                gsisId =datas['gsisId'],
                pagibigId =datas['pagibigId'],
                philhealthId =datas['philhealthId'],
                tinId =datas['tinId'],
                mobileNum =datas['mobileNum'],
                depedEmail =datas['depedEmail'],
                positionType =datas['positionType'],
                positionName =datas['positionName'],
                districtName =datas['districtName'],
                schoolName =datas['schoolName'],
            )
            return JsonResponse({
                "success": True,
            })
        return JsonResponse({
            "success": False,
            "message": form.errors
        })


def thankyou(request):
    return render(request, 'thankyou.html')




