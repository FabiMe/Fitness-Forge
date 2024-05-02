from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FAQ
from .forms import FAQForm

def faq_list(request):
    query = request.GET.get('q')
    if query:
        faqs = FAQ.objects.filter(Q(question__icontains=query) | Q(answer__icontains=query))
    else:
        faqs = FAQ.objects.exclude(answer='').order_by('-created_at')
    return render(request, 'faq/faq.html', {'faqs': faqs})

@login_required
def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.created_by = request.user
            faq.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'faq/add_faq.html', {'form': form})