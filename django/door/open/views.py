from django.shortcuts import render,HttpResponse
import pyrebase

Config = {
  "apiKey": "AIzaSyBVd86dWqmOt7a8Dz-Fr2JSoilS4_erLYk",
  "authDomain": "sur-iot6.firebaseapp.com",
  "databaseURL": "https://sur-iot6-default-rtdb.firebaseio.com",
  "projectId": "sur-iot6",
  "storageBucket": "sur-iot6.appspot.com",
  "messagingSenderId": "175280884318",
  "appId": "1:175280884318:web:02e7a40bcf9f6058a9c2cf",
  "measurementId": "G-GYESQC92T5"
}

firebase= pyrebase.initialize_app(Config)
authe= firebase.auth()
database= firebase.database()

# Create your views here.
def home(request):
    data= database.child("/").get().val()
    val=list(data.values())
    if(val[len(val)-1]['door']==0):
        val[len(val)-1]['door']='locked'
    else:
        val[len(val)-1]['door']='unlocked'
    return render(request,'home.html',{"database":val[len(val)-1]})

def contact(request):
    return HttpResponse("Created by shoubhik ghosh")



def history(request):
    data= database.child("/").get().val()
    val=list(data.values())
    length= len(val)
    for i in range(length):
        if(val[i]['door']==0):
            val[i]['door']='locked'
        else:
            val[i]['door']='unlocked'
          
    
    return render(request,'history.html',{"database":val})