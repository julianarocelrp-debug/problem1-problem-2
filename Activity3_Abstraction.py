from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(f"Sending Email: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"Sending SMS: {message}")


class AppNotification(Notification):

    def send(self, message):
        print(f"Sending App Notification: {message}")


# Create objects of all notification classes
notifications = [
    EmailNotification(),
    SMSNotification(),
    AppNotification()
]

# Message to be sent
message = "Enrollment is now open!"

# Send the message using each notification channel
for notification in notifications:
    notification.send(message)