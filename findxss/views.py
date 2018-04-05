from django.http import HttpResponse
from django.template import loader, Context
from django.utils.safestring import mark_safe


def index(request):
	return HttpResponse("Test!")

def firstchallenge(request):
	search_param = request.GET.get('search', '')

	template = loader.get_template('findxss/firstchallenge/index.html')
	context = {'search_param': mark_safe(search_param)}
	return createresponse(context, template, 'YOU_ARE_OWNED!')

def secondchallenge(request):
	colour_param = request.GET.get('colour', '#ff0000')

	template = loader.get_template('findxss/secondchallenge/index.html')
	context = {'colour_param': mark_safe(colour_param)}
	return createresponse(context, template, 'GOT_YOU_SECOND_TIME!')

def thirdchallenge(request):
	search_param = request.GET.get('search', '')

	search_param = search_param.replace('<script>', '')
	search_param = search_param.replace('</script>', '')

	print('search param:')
	print(search_param)

	template = loader.get_template('findxss/thirdchallenge/index.html')
	context = {'search_param': mark_safe(search_param)}
	return createresponse(context, template, 'WUT_I_FILTERED_SCRIPT_TAG!')

	
def createresponse(context, template, cookietext):
	response = HttpResponse(template.render(context))
	response['Set-Cookie'] = 'TEAM_42_LOGIN_SESSION=' + cookietext
	response['X-XSS-Protection'] = '0'
	return response