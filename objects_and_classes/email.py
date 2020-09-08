class Email:
    def __init__(self, sender, receiver, content, is_send=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


class MailBox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_emails(self, email_indexes):
        for index in email_indexes:
            self.emails[index].send()

    def print_mailbox(self):
        for email in self.emails:
            print(email.get_info())


mailbox = MailBox()

while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    mailbox.add_email(email)

# Send emails
emails_to_send = list(map(int, input().split(", ")))

# Mark email as sent
mailbox.send_emails(emails_to_send)

# Print emails
mailbox.print_mailbox()
