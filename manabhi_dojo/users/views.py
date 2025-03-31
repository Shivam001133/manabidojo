from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import Http404

from manabhi_dojo.users.forms import UserSignUpForm
from manabhi_dojo.users.models import User, Profile


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_absolute_url()

    def get_object(self, queryset: QuerySet | None = None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()


def home_view(request):
    return render(request, "index.html")


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Optional: Save avatar if provided
            avatar = form.cleaned_data.get('avatar')
            if avatar:
                user_profile = user.profile  # Assuming you have a related UserProfile model
                user_profile.avatar = avatar
                user_profile.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = UserSignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def get_user_progress(user):
    # Replace this with actual data fetching logic (e.g., from the database)
    return {
        'completed_lessons': 45,
        'current_streak': 7,
        'points_earned': 350,
        'n5_progress': 60,  # 60% progress on N5 course
    }


# @login_required
def dashboard(request):
    # Ensure the user is logged in before showing the dashboard
    if not request.user.is_authenticated:
        raise Http404("Page not found")

    user_progress = get_user_progress(request.user)  # Fetch the user's progress data

    return render(request, 'pages/dashboard.html', {
        'user_progress': user_progress,
        'user': request.user,  # Pass the user object to the template for personalization
    })


# @login_required
def profile_view(request):
    # Get the user's profile information
    user_profile = Profile.objects.get(user=request.user)

    # Pass the user profile and any other relevant data to the template
    return render(request, 'user/profile.html', {
        'user_profile': user_profile,
    })