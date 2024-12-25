from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserRegisterForm(UserCreationForm):
    pass

class UserLoginForm(AuthenticationForm):
    pass