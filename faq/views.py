from django.template.response import TemplateResponse
from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all()
    context = {'faqs': faqs}
    return TemplateResponse(request, 'faq.html', context)

def faq_detail(request, faq_id):
    faq = FAQ.objects.get(id=faq_id)
    return render(request, 'faq_detail.html', {'faq': faq})