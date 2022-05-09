from django.shortcuts import render, redirect

from dwitter.forms import DweetForm
from dwitter.models import Profile, Dweet


def dashboard(request):
    """Returns start page"""
    form = DweetForm(request.POST or None)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = user
            dweet.save()
            return redirect("dwitter:dashboard")

    followed_dweets = Dweet.objects.filter(
        user__profile__in=user.profile.follows.all()
    )
    return render(
        request,
        "dwitter/dashboard.html",
        {"form": form, "dweets": followed_dweets},
    )

def get_profile_list(request):
    """Return profiles list page """
    profiles = Profile.objects.exclude(user=request.user)

    return render(request, 'dwitter/profile_list.html', {'profiles': profiles})


def get_profile(request, pk):
    """Returns profiles page"""
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, 'dwitter/profile.html', {'profile': profile})
