# from django.db.models import signals
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings


# from .models import Contact

# @receiver(signals.post_save, sender=Contact, dispatch_uid="contact_create_log")
# def send_message(sender, instance, created, **kwargs):
#     print(instance.email)
#     subject = f'Thank {instance.name} for contact with us!'
#     message = 'Lorem Ipsum'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [instance.email]

#     send_mail( subject, message, email_from, recipient_list )