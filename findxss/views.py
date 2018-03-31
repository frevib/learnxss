from django.http import HttpResponse
from django.template import loader, Context
from django.utils.safestring import mark_safe


def index(request):
	return HttpResponse("Hello world. You're at the polls index.")

def testargument(request):
	id_query_param = request.GET.get('id')

	template = loader.get_template('findxss/index.html')
	context = {
		'id_query_param': id_query_param
	}

	context2 = {'id_query_param': mark_safe(id_query_param)}


	print('context:')
	print(context)

	# print('query param: ')
	# print(id_query_param)
	# return HttpResponse("The following ID is requested: %s" % id_query_param)
	return HttpResponse(template.render(context2))

