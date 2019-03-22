# Generated by Django 2.1.7 on 2019-03-22 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('completed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Day of the event')),
                ('start_time', models.TimeField(verbose_name='Starting time')),
                ('end_time', models.TimeField(verbose_name='Final time')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Textual Notes')),
                ('artist', models.IntegerField(choices=[(2, 'Kobay Kronik'), (1, 'Charly Reynoso'), (3, 'Shingken'), (4, 'Tyoni Aragon'), (5, 'Mat Moreno'), (6, 'Bookie'), (7, 'Owen Paulls'), (8, 'Matt Hildebrand'), (9, 'KC Kellman'), (10, 'Mike Devries')], default=(2, 'Kobay Kronik'))),
                ('location', models.IntegerField(choices=[(1, 'The Honorable Society'), (2, 'Rabble Rouser'), (3, 'Art & Soul Tattoo Co'), (4, 'Ink Monkey Tattoo and Piercing'), (5, 'Buzzbomb Tattoo and Body Piercing'), (6, 'House of Ink'), (7, 'Solid Gallery One'), (8, 'White Lotus Tattoo'), (9, 'Outer Limits Tattoo'), (10, '8th Element Tattoo'), (11, 'Agape Art Collective'), (12, 'Life After Death Tattoo')], default=(1, 'The Honorable Society'))),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
        migrations.CreateModel(
            name='JoinTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.IntegerField()),
                ('tattoo', models.IntegerField()),
                ('artist', models.IntegerField()),
                ('profile', models.IntegerField()),
                ('location', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street', models.TextField(max_length=240)),
                ('city', models.TextField(max_length=50)),
                ('state', models.TextField(max_length=2)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(default=None, max_length=150)),
                ('phone_number', models.CharField(default=None, max_length=100)),
                ('tattoo', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tattoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=240)),
                ('url', models.CharField(default='', max_length=100)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]