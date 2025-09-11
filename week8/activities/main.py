import asynchronous
import decorators
import factory
import observer


if __name__ == '__main__':
    observer = observer.UploadNotifier()
    observer.subscribe(factory.create_user)
    user = factory.create_user("admin", "Zac")
    user2 = factory.create_user("editor", "Ben")
    user3 = factory.create_user("viewer", "Lucinda")
    observer.notify(observer.alert_admin("misc.doc"))
