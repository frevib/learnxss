from django.http import HttpResponse
from django.template import loader, Context
from django.utils.safestring import mark_safe


def index(request):
	return HttpResponse("TestQQQ")

def firstchallenge(request):
	search_param = request.GET.get('search', '')

	template = loader.get_template('findxss/firstchallenge/index.html')
	context = {'search_param': mark_safe(search_param)}
	return createresponse(context, template)

def secondchallenge(request):
	search_param = request.GET.get('search', '')

	template = loader.get_template('findxss/secondchallenge/index.html')
	context = {'search_param': mark_safe(search_param)}
	return createresponse(context, template)

	
def createresponse(context, template):
	response = HttpResponse(template.render(context))
	response['Set-Cookie'] = 'TEAM_42_LOGIN_SESSION=YOU_ARE_OWNED!'
	response['X-XSS-Protection'] = '0'
	return response