from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from main_app.forms import ContactForm, ServiceRequestForm
from django.contrib import messages
from main_app.models import Service, Company


def landing_page(request):
    services = Service.objects.filter(display=True)
    return render(request, 'main_app/landing.html', context={
        'services': services
    })


def about_us(request):
    our_company = Company.objects.latest('created')
    return render(request, 'main_app/about.html',
                  context={'our_company': our_company})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent")
        else:
            messages.error(request, "Error in submitted message")
    else:
        form = ContactForm()

    return render(request, 'main_app/contact.html', context = {
        'form': form,
    })


def service_request(request, service_slug):
    try:
        service = Service.objects.get(slug=service_slug)
        if request.method == 'POST':
            form = ServiceRequestForm(request.POST)
            if form.is_valid():
                form.instance.parent_service = service
                form.save()
                messages.success(request, "We've successfully received your request.")
                return HttpResponseRedirect("")
            else:
                messages.error(request, "There was an error submitting your request, "
                                        "please try again!")
        else:
            form = ServiceRequestForm()
    except Service.DoesNotExist:
        return HttpResponse('Error 404: The selected service does not exist.')
    return render(request, 'main_app/service_request.html', context={
        'service': service,
        'form': form
    })


def subscribe(request):
    return render(request, 'main_app/subscribe.html')


def unsubscribe(request):
    return render(request, 'main_app/unsubscribe.html')
