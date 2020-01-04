from django.shortcuts import render,get_object_or_404
from .models import Contact
from django.views.generic import ListView,DetailView

# Create your views here.
# def index(request):
# 	contacts = Contact.objects.all
# 	return render(request,'index.html',{'contacts':contacts})
class HomeListView(ListView):
	template_name = 'index.html'
	model = Contact
	context_object_name = 'contacts'
class DetailDetailView(DetailView):
	template_name = 'detail.html'
	model = Contact
	context_object_name = 'contacts'

# def detail(request, id):
# 	contacts = get_object_or_404(Contact, pk=id)
# 	return render(request, 'detail.html',{'contacts':contacts})