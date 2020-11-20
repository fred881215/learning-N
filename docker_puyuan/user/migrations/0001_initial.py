# Generated by Django 2.1 on 2020-08-15 05:43

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fb_id', models.CharField(blank=True, max_length=100)),
                ('invite_code', models.CharField(max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=100)),
                ('emailck', models.BooleanField(default=True)),
                ('FBck', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='deflat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('sugar_dalta_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_delta_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_morning_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_morning_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_evening_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_evening_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_before_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_before_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_after_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('sugar_after_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('systolic_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('systolic_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('diastolic_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('diastolic_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('pulse_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('pulse_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('weight_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('weight_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('bmi_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('bmi_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('body_fat_max', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('body_fat_min', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='druginformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('drugname', models.CharField(blank=True, max_length=50, null=True)),
                ('drugtype', models.CharField(default='0', max_length=1)),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HbA1c',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('a1c', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='medicalinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('user_id', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('diabetes_type', models.DecimalField(decimal_places=0, default=0, max_digits=15)),
                ('oad', models.CharField(default='0', max_length=1)),
                ('insulin', models.CharField(default='0', max_length=1)),
                ('anti_hypertensivers', models.CharField(default='0', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('member_id', models.CharField(blank=True, max_length=100)),
                ('reply_id', models.CharField(blank=True, max_length=100)),
                ('message', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('fid', models.CharField(blank=True, max_length=100)),
                ('data_type', models.CharField(blank=True, max_length=100)),
                ('relation_type', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=16, max_digits=19, null=True)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('fcm_id', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('weight', models.DecimalField(blank=True, decimal_places=16, max_digits=19, null=True)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pushed_at', models.DateTimeField(auto_now=True)),
                ('unread_records_one', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('unread_records_two', models.CharField(blank=True, default='0', max_length=100)),
                ('unread_records_three', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('verified', models.CharField(default='0', max_length=10)),
                ('privacy_policy', models.CharField(default='0', max_length=10)),
                ('must_change_password', models.BooleanField(default=False)),
                ('status', models.CharField(default='Normal', max_length=100)),
                ('login_times', models.DecimalField(decimal_places=0, default='0', max_digits=15)),
                ('after_recording', models.CharField(default='0', max_length=1)),
                ('no_recording_for_a_day', models.CharField(default='0', max_length=1)),
                ('over_max_or_under_min', models.CharField(default='0', max_length=1)),
                ('after_mael', models.CharField(default='0', max_length=1)),
                ('unit_of_sugar', models.CharField(default='0', max_length=1)),
                ('unit_of_weight', models.CharField(default='0', max_length=1)),
                ('unit_of_height', models.CharField(default='0', max_length=1)),
                ('badge', models.DecimalField(decimal_places=0, default='0', max_digits=15)),
                ('group', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]