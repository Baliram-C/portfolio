from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'portfolio_app/index.html')

def about(request):
    return render(request, 'portfolio_app/about.html')

def contact(request):
    return render(request, 'portfolio_app/contact.html')

def portfolio(request):
    return render(request, 'portfolio_app/portfolio.html')

def portfolio_details(request):
    return render(request, 'portfolio_app/portfolio-details.html')

def resume(request):
    return render(request, 'portfolio_app/resume.html')

def services(request):
    return render(request, 'portfolio_app/services.html')

def service_details(request):
    return render(request, 'portfolio_app/service-details.html')

def starter_page(request):
    return render(request, 'portfolio_app/starter-page.html')

##for submitting the details query
def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # You can save the data to a model or send an email
        # Example: Sending email
        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,  # From email (configured in settings.py)
                ['baliram.chaudhari51@gmail.com'],  # To email
                fail_silently=False,
            )
            return HttpResponse('Message sent successfully!')
        except Exception as e:
            return HttpResponse(f'Failed to send message: {e}')

    return redirect('contact_page')  # Redirect to contact page or any other
