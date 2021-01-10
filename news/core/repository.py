from .models import Contact


class Repo:

    def create_contact(self, payload):
        new_contact = Contact(
            name = payload.name,
            email = payload.email,
            subject = payload.subject,
            message = payload.message
        )
        new_contact.save()

        return new_contact