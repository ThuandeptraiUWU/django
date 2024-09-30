# Generated by Django 5.1.1 on 2024-09-26 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0010_alter_fruit_options_alter_manufacturer_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nhập tên địa điểm', max_length=50)),
                ('address', models.CharField(help_text='Nhập địa chỉ', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='newapp.place')),
                ('serves_hot_dogs', models.BooleanField(default=False, help_text='Có phục vụ hot dog không?')),
                ('serves_pizza', models.BooleanField(default=False, help_text='Có phục vụ pizza không?')),
            ],
            bases=('newapp.place',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='newapp.place')),
                ('customers', models.ManyToManyField(help_text='Chọn các khách hàng của nhà cung cấp', related_name='providers', to='newapp.place')),
            ],
            bases=('newapp.place',),
        ),
    ]
