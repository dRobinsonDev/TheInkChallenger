# Generated by Django 2.1.5 on 2019-03-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190321_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='artist',
            field=models.IntegerField(choices=[(2, 'Kobay Kronik'), (1, 'Charly Reynoso'), (3, 'Shingken'), (4, 'Tyoni Aragon'), (5, 'Mat Moreno'), (6, 'Bookie'), (7, 'Owen Paulls'), (8, 'Matt Hildebrand'), (9, 'KC Kellman'), (10, 'Mike Devries')], default=2),
        ),
    ]
