from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# 33. Adding & Registering Templates
# from django.template.loader import render_to_string

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
    list_items = ''
    for month in monthly_challenges.keys():
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    return HttpResponse(f'<ul>{list_items}</ul>')


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month-1]

    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


# def monthly_challenge_33(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         # 33. Adding & Registering Templates
#         response_data = render_to_string('challenges/challenge.html')
#     except:
#         return HttpResponseNotFound('<h1>This month is not supported!</h1>')
#     return HttpResponse(response_data)


# def monthly_challenge_34(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         # 34. Rendering Templates
#         return render(request, 'challenges/challenge.html')
#     except:
#         return HttpResponseNotFound('<h1>This month is not supported!</h1>')


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # 35. Template Language
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            # 36
            'month_name_36': month.capitalize(),
            # 37. Filters
            'month_name': month
        })
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
