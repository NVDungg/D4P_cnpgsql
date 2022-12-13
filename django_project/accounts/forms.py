from django.contrib.auth import get_user_model  #which looks to our AUTH_USER_MODEL config in settings.py
#https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')