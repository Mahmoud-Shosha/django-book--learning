from django.http import HttpResponse
import datetime

def hello(request):

	return HttpResponse('Hello World !')

def current_datetime(request):
	now = datetime.datetime.now()
	output = '<html><body>It is now : &nbsp;&nbsp;{}</body></html>'.format(now)
	return HttpResponse(output)

def hours_ahead(request, offset):
	print(type(offset)) # int
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	# assert False
	output = '<html><body>It is : &nbsp;&nbsp;{}<br><br> As It is offset by {} </body></html>'.format(dt, offset)
	return HttpResponse(output)