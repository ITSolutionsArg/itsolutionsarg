from django.shortcuts import render_to_response

def menu(request):
	response = render_to_response('index.html')	
	return response

