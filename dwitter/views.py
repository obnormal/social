from django.shortcuts import render

from dwitter.models import Profile


def dashboard(request):
    """Returns start page"""
    return render(request, 'dwitter/dashboard.html')


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
