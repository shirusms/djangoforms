from django import forms
from myapp.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
