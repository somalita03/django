# Generated by Django 4.2.5 on 2023-10-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='calc.tag'),
        ),
    ]
