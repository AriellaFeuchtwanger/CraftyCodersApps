from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template import RequestContext
from captcha.fields import CaptchaField
# Create your forms here.


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject,
            msg,
            'ariella@craftycodersapps.com',
            [settings.RECIPIENT_ADDRESS]
        )
