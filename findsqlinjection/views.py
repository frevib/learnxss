from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, Context
from django.utils.safestring import mark_safe

def test(request):
	return HttpResponse("w000t just testing!!")