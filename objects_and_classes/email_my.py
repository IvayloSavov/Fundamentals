class MailBox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_emails(self, emails_to_send):
        for index in emails_to_send:
            self.emails[index].send()

    def print_emails(self):
        for email in self.emails:
            print(email.get_info())


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


mailbox = MailBox()

while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    mailbox.add_email(email)

# Indices to send
emails_to_send = list(map(int, input().split(", ")))

# Sending emails
mailbox.send_emails(emails_to_send)

# Printing output
mailbox.print_emails()