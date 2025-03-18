from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from django.core.mail import send_mail
print("signals.py LOADED!")  # Debugging print


@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, created, **kwargs):
    if created:  # Only send email when a new Contact is created
        print(f"Signal Triggered: Sending email for {instance.email}")  # Debugging statement

        send_mail(
            'New Client',
            f'Name: {instance.name}\nEmail: {instance.email}\nPhone: {instance.phone}\n\nRequirement: {instance.remarks}\n\n\n\n Thanks and Regards JAS.com',
            'helpdesk.team.it@gmail.com',
            ['vrules58@gmail.com'],
            fail_silently=False  # Raise error if email fails
        )

        # send_mail(
        #     'New Client',
        #     f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nRequirement: {remarks}\n\n\n\n Thanks and Regards JAS.com',
        #     'helpdesk.team.it@gmail.com',
        #     ['vrules58@gmail.com']
        # )