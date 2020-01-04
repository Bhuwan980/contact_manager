from django.shortcuts import render,get_object_or_404
from .models import Contact

# Create your views here.
def index(request):
	contacts = Contact.objects.all
	return render(request,'index.html',{'contacts':contacts})

def detail(request, id):
	contacts = get_object_or_404(Contact, pk=id)
	return render(request, 'detail.html',{'contacts':contacts})