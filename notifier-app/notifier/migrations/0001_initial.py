from django.db import migrations, models

<<<<<<< HEAD:week11/notifier_app/notifier/migrations/0001_initial.py
=======

>>>>>>> b30f28154bce28dd6ce11676eb05caacfb848c64:week11/notifier-app/notifier/migrations/0001_initial.py
class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
<<<<<<< HEAD:week11/notifier_app/notifier/migrations/0001_initial.py
                ("id", models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ]
        )
    ]
=======
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
>>>>>>> b30f28154bce28dd6ce11676eb05caacfb848c64:week11/notifier-app/notifier/migrations/0001_initial.py
