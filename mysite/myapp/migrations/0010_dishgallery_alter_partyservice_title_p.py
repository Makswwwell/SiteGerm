# Generated by Django 4.2.9 on 2024-01-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_partyservice_title_p'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default_image.jpg', upload_to='gallery/')),
            ],
        ),
        migrations.AlterField(
            model_name='partyservice',
            name='title_p',
            field=models.CharField(max_length=255),
        ),
    ]
