from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january":"Hola January",
    "february":"Hi February",
    "march": None

} 

def index(request):
    months = list (monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months":months
    } )

def monthly_challenge_by_number(request, month):
    months = list (monthly_challenges.keys())
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try: 
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)