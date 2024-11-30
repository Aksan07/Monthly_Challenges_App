from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_dic = {
    "january":"Learn",
    "february":"Work Hard",
    "march": "Pray Hard",
    "april": "Keep Going",
    "may":"Fight On",
    "june":"Understand Defeat",
    "july":"Become Better",
    "august":"Live for God",
    "september": "Stay Humble", 
    "october":"He didnot abandon you",
    "november":"Sacrifice the evil in your heart",
    "december":None,
                      }

# Create your views here.
def index(request):
    month_key =list(monthly_challenges_dic.keys())
    return render (request,"challenges/index.html",{
        "months_list":month_key
    })


def monthly_challenges_int(request,month):
    
    months = list(monthly_challenges_dic.keys())
    if month >len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirect_url =reverse("month-challenge",args=[redirect_month])
    
    return HttpResponseRedirect(redirect_url)

def monthly_challenges(request,month):
    try:
        challenge_text = monthly_challenges_dic[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month":month,
        })

    except KeyError:
        return HttpResponseNotFound("<h1>Believe Man, God Bless Your Soul</h1>")
