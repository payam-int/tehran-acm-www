import re
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from account.models import StudentField
from account.validators import validate_student_id


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', required=True)
    field = forms.ModelChoiceField(queryset=StudentField.objects.all())
    student_id = forms.IntegerField(validators=[validate_student_id])

    def validate(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if User.objects.filter(email=email).exclude(username=username).exists() or re.match(
                r'^([A-Z|a-z|0-9](\.|_){0,1})+[A-Z|a-z|0-9]\@ut.ac.ir$', email):
            raise forms.ValidationError(u'Invalid data.')



    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
