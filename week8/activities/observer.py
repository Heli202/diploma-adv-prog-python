import logging


class UploadNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, function_passed):
        self.subscribers.append(function_passed)

    def notify(self, event):
        for function_passed in self.subscribers:
            function_passed(event)

    def alert_admin(doc):
        logging.info(f"Alert admin: {doc} was uploaded.")

