from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from board.models import Author


class RegisterUserForm(SignupForm):
    def save(self, request):
        user = super(RegisterUserForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        if not Author.objects.filter(user=user).exists():
            Author.objects.create(user=user)
        return user
