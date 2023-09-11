from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# 25. More Dynamic View Logic
monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'feburary': 'Work for at least 20 minutes every day!',
    'march': 'Do it!',
    'april': 'Do it!',
    'may': 'Do it!',
    'june': 'Do it!',
    'july': 'Do it!',
    'august': 'Do it!',
    'september': 'Do it!',
    'october': 'Do it!',
    'november': 'Do it!',
    'december': 'Do it!'
}


def index(request):
    # 29. Practice
    list_items = ''
    for month in monthly_challenges.keys():
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    return HttpResponse(f'<ul>{list_items}</ul>')

# def index(request):
#     # 21.
#     return HttpResponse('This works!')


# def janurary(request):
#    # 22.
#    return HttpResponse('Eat no meat for the entire month!')

# def february(request):
#    # 22.
#    return HttpResponse('Work for at least 20 minutes every day!')


def monthly_challenge_23(request, month):

    # 23.
    if month == 'january':
        challenge_text = 'Eat no meat for the entire month!'
    elif month == 'feburary':
        challenge_text = 'Work for at least 20 minutes every day!'
    else:
        return HttpResponseNotFound('This month is not supported!')

    return HttpResponse(challenge_text)


def monthly_challenge_by_number(request, month):
    # 24. Path Segments
    # return HttpResponse(month)

    # 26. Redirects
    # Nowadays, Python dicts are ordered.
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month-1]
    # return HttpResponseRedirect('/challenges/' + redirect_month)

    # 27. Reverse Function & Named URLs
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # 25. More Dynamic View Logic
    try:
        challenge_text = monthly_challenges[month]
        # 28. HTML
        # String interpolation / f-Strings
        response_data = f'<h1>{challenge_text}</h1>'
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')

    return HttpResponse(response_data)
