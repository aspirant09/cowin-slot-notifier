from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse
import requests

from .models import UserDetails



def login(request):
    username=""
    if request.method=='GET':
        form=UserForm()
        return render(request,"index.html",{"form":form})
    else:
        form=UserForm(request.POST)
        if form.is_valid():
            saveData=form.save(commit=False)
            data=request.POST
            if len(saveData.pinCode)==0:
                fetchStateAndDistrictData(data,saveData)
            saveData.save()
            return redirect(reverse("location",kwargs={"username":saveData.username}))
    return HttpResponse("Somethings wrong")



def locationSelect(request,username):
    return HttpResponse("Thanks for subscribing "+username)


def fetchStateAndDistrictData(formDdata,userData):
    headers={
                "accept": "application/json",
                "Accept-Language": "hi_IN",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
            }
    url="https://cdn-api.co-vin.in/api/v2/admin/location/states"
    response = requests.get(url, headers=headers)
    print("Fetching state value... ",response)
    data=response.json()
    states=data['states']
    for stateData in states:
        if stateData['state_name']==formDdata['state']:
            userData.state=str(stateData['state_id'])
            break
    
    url="https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+userData.state
    response = requests.get(url, headers=headers)
    print("Fetching district value... ",response)
    data=response.json()
    districts=data['districts']
    for districtData in districts:
        if districtData['district_name']==formDdata['district']:
            userData.district=str(districtData['district_id'])
            break
  
    