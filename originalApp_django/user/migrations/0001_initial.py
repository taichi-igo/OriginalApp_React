# Generated by Django 3.0.7 on 2020-06-21 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='ニックネーム')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('birthday', models.DateField(null=True, verbose_name='生年月日')),
                ('address', models.CharField(max_length=140, null=True, verbose_name='現住所')),
                ('password', models.CharField(max_length=140, verbose_name='パスワード')),
                ('is_tmp_user', models.BooleanField(default=False)),
                ('occupation_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.Occupation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
