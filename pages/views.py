from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms
# from django.core.mail import send_mail, get_connection

from . models import Page
# from .forms import ContactForm

def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=Fales, label='Your E-mail Address')
    messages =forms.CharField(widget=forms.Textarea)
    
