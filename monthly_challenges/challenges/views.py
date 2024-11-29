from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

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
    "december":"Kill Lust",
                      }

# Create your views here.
def index(request):
    list_items =''
    month_key =list(monthly_challenges_dic.keys())
    for month in month_key:
        month_url =reverse("month-challenge",args=[month])
        list_items+=f'<li><a href="{month_url}">{month}</a></li>'
    return HttpResponse(f"<ul>{list_items}</ul>")


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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("<h1>Believe Man, God Bless Your Soul</h1>")
