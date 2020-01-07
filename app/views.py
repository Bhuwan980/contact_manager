from django.shortcuts import render,redirect
from .models import Contact
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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

def search(request):
	if request.GET:
		
		search_term = request.GET['search_text']
		search_result = Contact.objects.filter( Q(name__icontains=search_term)|
		Q(email__icontains=search_term)|
		Q(phone__iexact=search_term)|
		Q(info__icontains=search_term)
		)
		context = {'search_term':search_term,
		'contacts':search_result
		}
		return render(request,'search.html',context)
	else:
		return redirect('index')

class ContactCreateView(CreateView):
	model = Contact
	template_name = 'create.html'
	fields = ['name','phone','info','email','image','gender']
	success_url = '/'
class ContactUpdateView(UpdateView):
	model = Contact
	template_name='update.html'
	fields = ['name','phone','info','email','image','gender']
	
	def form_valid(self,form):
		instance = form.save()
		return redirect ('detail',instance.pk)

class ContactDeleteView(DeleteView):
	model = Contact
	template_name='delete.html'
	success_url = '/'

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username=username,password=password)
		if user is not None:
			messages.success(request, ('you successfully logged in!'))
			login(request, user)
			return redirect('index')
		else:
			messages.success(request, ("User doesn't exist!"))
			return redirect('login')
	else:
		return render(request, 'login.html',{})

	
def logout_user(request):
	logout(request)
	messages.success(request, ("Logged out!"))
	return redirect('index')

def register_user(request):
	if request.method == 'POST':
		if request.POST['password']==request.POST['password1']:
			try:
				user = User.objects.get(username=request.POST['username'])
				messages.success(request,('username is already taken!'))
				return redirect('register')
			except User.DoesNotExist:
				user = User.objects.create_user(request,request.POST['username'],request.POST['password'])
				login(request,user)
				messages.success(request,('successfully registered!'))
				return redirect('index')
	else:
		return render(request,'register.html')