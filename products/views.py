from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm
from comments.forms import CommentForm


def all_products(request):
    """A view to show all products, including sorting and search queries, excluding mystery boxes"""
    products = Product.objects.filter(is_mystery_box=False)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
        "meta_description": "Browse our collection of products, filter by categories, and find the perfect item for you.",
    }

    return render(request, "products/products.html", context)


def product_detail(request, pk):
    """A view to show individual product details, and handle comments"""
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect("product_detail", pk=pk)
        else:
            messages.error(request, "Error adding your comment. Please check the form.")
    else:
        comment_form = CommentForm()

    context = {
        "product": product,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
        "meta_description": f"Discover more about {product.name} and read reviews from other customers.",
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store"""
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("add_product"))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {"form": form, "meta_description": "Add a new product to the store."}

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
        "meta_description": f"Edit the details of {product.name}.",
    }

    return render(request, template, context)


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
