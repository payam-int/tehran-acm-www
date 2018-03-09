from django.contrib.auth.forms import UserCreationForm
from django.forms import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
