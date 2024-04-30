from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from profiles.forms import UserProfileForm
from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)

@login_required
def profile_update(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_update') 
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profiles/profile_update.html', {'form': form})