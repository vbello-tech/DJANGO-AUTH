from django.shortcuts import render

# Create your views here.

def UserProfile(request):
    context = {
        'user':request.user
    }
    return render(request, 'registrations/profile.html', context)



