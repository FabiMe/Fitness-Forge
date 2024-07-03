from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the request user is an admin or the comment owner
    if request.user.is_admin or request.user == comment.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(request, "You do not have permission to delete this comment.")

    # Redirect to a success page, or back to comment page with a message
    return redirect("product_detail")


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment added!")
            return redirect("product_detail")
    else:
        form = CommentForm()
    return render(request, "product_detail.html", {"comment_form": form})