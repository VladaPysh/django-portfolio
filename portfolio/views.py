from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.

def index(request):
  form = ContactForm()
  return render(request, "portfolio/index.html", {
    'form': form
  })

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      subject = "Contact form"
      body = {
			'name': form.cleaned_data['name'],
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
      message = "\n".join(body.values())
      
      try:
        send_mail(subject, message, 'admin@example.com', ['vlada.pysh1@gmail.com']) 
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      return redirect ("index")
  
  form = ContactForm()
  return render(request, "portfolio/index.html", {'form':form})