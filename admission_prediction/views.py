from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import joblib
import datetime
from django.templatetags.static import static


def index(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return render(request, "index.html")


def result(request):

    if(request.method == "POST"):
        gre = int(request.POST.get('gre_score'))
        toefl = int(request.POST.get('toefl'))
        uni_rating = int(request.POST.get('university_rating'))
        cgpa = float(request.POST.get('cgpa'))
        
        data = []
        data.append(gre)
        data.append(toefl)
        data.append(uni_rating)
        data.append(cgpa)

        print(data)

        MODEL_PATH = 'admission_prediction.sav'
        loaded_model = joblib.load(open(MODEL_PATH,'rb'))
        
        result = loaded_model.predict([data])
        result = result[0][0] * 100
        result = ("%.2f" % result)
        print(result)
        cxt ={'result':result}
        return render(request, 'result.html',cxt)
    return HttpResponseRedirect('/')
   