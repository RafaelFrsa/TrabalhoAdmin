from django.shortcuts import render
"""from sistema.core.forms import PostForm"""

def home(request):

	return render(request, 'home.html')
	