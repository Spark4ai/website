from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactSubmission
def index(request):
    return render(request, 'index.html')
def projects(request):
    return render(request, 'project.html')
def council(request):
    return render(request, 'aicouncil.html')
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the submission to the database
        submission = ContactSubmission(name=name, email=email, subject=subject, message=message)
        submission.save()


        return JsonResponse({'message': 'Your message has been sent. Thank you!'})
    return render(request, 'index.html')
# Create your views here.
