# Generated by Django 4.1.7 on 2023-03-31 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_add_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_complaint',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='add_complaint',
            name='status',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
