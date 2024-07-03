from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FAQ
from .forms import FAQForm
from django.db.models import Q
from django.contrib import messages


def faq_list(request):
    query = request.GET.get("q")
    if query:
        faqs = FAQ.objects.filter(
            Q(question__icontains=query) | Q(answer__icontains(query))
        )
        meta_description = "Search results for FAQs."
    else:
        faqs = FAQ.objects.exclude(answer="").order_by("-created_at")
        meta_description = "Frequently asked questions about our services and products."
    return render(
        request, "faq/faq.html", {"faqs": faqs, "meta_description": meta_description}
    )


@login_required
def add_faq(request):
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.created_by = request.user
            faq.save()
            messages.success(
                request,
                "FAQ added! Please note that the question will be displayed after approval.",
            )
            return redirect("faq_list")
    else:
        form = FAQForm()
    context = {"form": form, "meta_description": "Add a new FAQ to help our users."}
    return render(request, "faq/add_faq.html", context)
