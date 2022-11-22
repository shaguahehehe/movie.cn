# Generated by Django 2.2.28 on 2022-06-23 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('add_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('info', models.TextField()),
                ('logo', models.CharField(max_length=100)),
                ('star', models.IntegerField()),
                ('play_nums', models.IntegerField()),
                ('comment_nums', models.IntegerField()),
                ('area', models.CharField(max_length=200)),
                ('release_time', models.DateField()),
                ('length', models.CharField(max_length=200)),
                ('add_time', models.DateTimeField()),
                ('download_url', models.CharField(max_length=300)),
                ('movie_file', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'film_movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmMoviecol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_moviecol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmPreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_preview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('info', models.CharField(blank=True, max_length=1024, null=True)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
                ('play_num', models.IntegerField(blank=True, null=True)),
                ('area', models.CharField(blank=True, max_length=255, null=True)),
                ('length', models.CharField(blank=True, max_length=255, null=True)),
                ('addtime', models.DateTimeField(blank=True, null=True)),
                ('updatetime', models.DateTimeField(blank=True, null=True)),
                ('movie_file', models.CharField(blank=True, max_length=255, null=True)),
                ('download_url', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('star', models.CharField(blank=True, max_length=255, null=True)),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('moive_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersUserlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('add_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'users_userlog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersUserprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=6)),
                ('info', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField()),
                ('uuid', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'users_userprofile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersUserprofileGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'users_userprofile_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersUserprofileUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'users_userprofile_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XadminBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url_name', models.CharField(max_length=64)),
                ('query', models.CharField(max_length=1000)),
                ('is_share', models.IntegerField()),
            ],
            options={
                'db_table': 'xadmin_bookmark',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XadminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('ip_addr', models.CharField(blank=True, max_length=39, null=True)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.CharField(max_length=32)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'xadmin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XadminUsersettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=256)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'xadmin_usersettings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XadminUserwidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.CharField(max_length=256)),
                ('widget_type', models.CharField(max_length=50)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'xadmin_userwidget',
                'managed': False,
            },
        ),
    ]