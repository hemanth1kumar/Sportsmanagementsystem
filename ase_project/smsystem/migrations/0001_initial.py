# Generated by Django 2.1.2 on 2018-10-26 07:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('announcement_id', models.AutoField(primary_key=True, serialize=False)),
                ('receiver', models.CharField(max_length=50)),
                ('sender', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('coach_id', models.AutoField(primary_key=True, serialize=False)),
                ('coach_name', models.CharField(max_length=50)),
                ('coach_type', models.CharField(max_length=50)),
                ('experience', models.IntegerField(default=0)),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('about', models.CharField(max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('performance_score', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.AutoField(default='', primary_key=True, serialize=False)),
                ('venue', models.CharField(default='iiits', max_length=50)),
                ('result', models.CharField(max_length=50, null=True)),
                ('opponent_1', models.CharField(max_length=50)),
                ('opponent_2', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('sport_id', models.AutoField(primary_key=True, serialize=False)),
                ('sport_name', models.CharField(max_length=50)),
                ('equipment', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('no_of_players', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('tournament_id', models.AutoField(primary_key=True, serialize=False)),
                ('tournament_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('level', models.CharField(max_length=50)),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Sport')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Sport'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Tournament'),
        ),
        migrations.AddField(
            model_name='player',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Sport'),
        ),
        migrations.AddField(
            model_name='player',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Student'),
        ),
        migrations.AddField(
            model_name='performance',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Sport'),
        ),
        migrations.AddField(
            model_name='performance',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Student'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Student'),
        ),
        migrations.AddField(
            model_name='coach',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsystem.Sport'),
        ),
    ]
