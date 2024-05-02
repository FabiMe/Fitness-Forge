from django.shortcuts import render
from products.views import product_detail
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the request user is an admin or the comment owner
    if request.user.is_admin or request.user == comment.user:
        comment.delete()
        message = "Comment deleted successfully."
    else:
        message = "You do not have permission to delete this comment."

    # Redirect to a success page, or back to comment page with a message
    return redirect('product_detail')  