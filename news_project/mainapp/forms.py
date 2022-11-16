from django.forms import ModelForm

from mainapp.models import Comments, Mail


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control p-3 {name} '
            item.help_text = ''

class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control p-3 {name} '
            item.help_text = ''