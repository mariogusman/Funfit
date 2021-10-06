from django.shortcuts import render

# Create your views here.

def profile(request):
    """ shows user's profile """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)