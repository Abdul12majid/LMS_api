# Generated by Django 5.1 on 2024-09-05 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lms_app", "0006_book_borrower_alter_book_publication_date_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="book_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="book",
            name="publication_date",
            field=models.DateField(
                default=datetime.datetime(2024, 9, 5, 15, 46, 5, 351274)
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="books_borrowed",
            field=models.ManyToManyField(
                blank=True, related_name="borrowed_books", to="lms_app.book"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="date_modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
