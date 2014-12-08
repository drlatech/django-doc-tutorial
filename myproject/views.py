# coding=utf-8
__author__ = 'zerocode'
from django.shortcuts import render_to_response
from django.template import RequestContext
from reportlab.pdfgen import canvas
from django.http import  HttpResponse
def home(request):
    return render_to_response('home.html', RequestContext(request))

def report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="xxx.pdf"'

    p = canvas.Canvas(response)
    p.drawString(10,100,'Ovo je pokušaj generisanja pdf-a.\nSve što se kreira biće super.\n\nDražen Lazarević')
    p.showPage()
    p.save()
    return response
