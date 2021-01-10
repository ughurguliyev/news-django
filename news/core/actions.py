from stories import story, arguments, Success, Failure, Result
from django.core.mail import send_mail
from django.conf import settings

from .repository import Repo
from .entities import Contact

class ContactCreation:

    @story
    @arguments('name', 'email', 'subject', 'message')
    def create(I):

        I.validate_input
        I.build_entity
        I.create_contact
        I.send_email
        I.done

    def validate_input(self, ctx):
        return Success()

    def build_entity(self, ctx):
        ctx.entity = Contact(
            name = ctx.name,
            email = ctx.email,
            subject = ctx.subject,
            message = ctx.message
        )
        return Success()
    
    def create_contact(self, ctx):
        ctx.result = Repo().create_contact(payload=ctx.entity)
        return Success()
    
    def send_email(self, ctx):
        subject = f'Thank {ctx.entity.name} for contacting us!'
        message = 'Lorem Ipsum'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [ctx.entity.email]

        send_mail( subject, message, email_from, recipient_list )
        return Success()
    
    def done(self, ctx):
        return Result(ctx.result)
    
