from django import forms
from .models import Contato
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class ContatoForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('emissor', css_class='form-group col-md-6'),
                Column('assunto', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'msg'
        )
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))
        
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', )
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model =  CustomUser
        fields = ('username', 'email', )