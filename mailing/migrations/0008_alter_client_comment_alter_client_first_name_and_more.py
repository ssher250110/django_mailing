# Generated by Django 4.0 on 2024-06-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_alter_client_comment_alter_client_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество'),
        ),
    ]
