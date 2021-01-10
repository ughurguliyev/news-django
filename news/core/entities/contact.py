from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    email: str
    subject: str
    message: str