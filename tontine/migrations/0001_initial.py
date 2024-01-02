# Generated by Django 4.1.4 on 2023-01-18 10:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id_membre', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25, null=True, unique=True)),
                ('prenom', models.CharField(blank=True, max_length=25, null=True)),
                ('e_mail', models.EmailField(blank=True, max_length=50, null=True)),
                ('adresse', models.CharField(max_length=15)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('date_naissance', models.DateField(null=True)),
                ('profession', models.CharField(max_length=25, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Membre',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id_poste', models.AutoField(primary_key=True, serialize=False)),
                ('nom_poste', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'Poste',
            },
        ),
        migrations.CreateModel(
            name='Tontine',
            fields=[
                ('id_tontine', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=15)),
                ('date_creation', models.DateField()),
                ('slogan', models.CharField(blank=True, max_length=100, null=True)),
                ('regle', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Tontine',
            },
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id_reunion', models.AutoField(primary_key=True, serialize=False)),
                ('date_reunion', models.DateField()),
                ('beneficiare', models.IntegerField()),
                ('lieu', models.CharField(max_length=25)),
                ('heure', models.TimeField()),
                ('regle', models.CharField(blank=True, max_length=1000, null=True)),
                ('motif', models.CharField(blank=True, max_length=100, null=True)),
                ('id_tontine', models.ForeignKey(db_column='id_tontine', on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine')),
            ],
            options={
                'db_table': 'Reunion',
            },
        ),
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id_pret', models.AutoField(primary_key=True, serialize=False)),
                ('nom_pret', models.CharField(blank=True, max_length=25, null=True)),
                ('date_pret', models.DateField()),
                ('montant', models.IntegerField()),
                ('date_remboursement', models.DateField()),
                ('interet', models.IntegerField()),
                ('sanction', models.IntegerField()),
                ('raison', models.CharField(blank=True, max_length=100, null=True)),
                ('id_membre', models.ForeignKey(db_column='id_membre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_tontine', models.ForeignKey(db_column='id_tontine', on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine')),
            ],
            options={
                'db_table': 'Pret',
            },
        ),
        migrations.CreateModel(
            name='Fond',
            fields=[
                ('id_fond', models.AutoField(primary_key=True, serialize=False)),
                ('type_fond', models.CharField(max_length=25)),
                ('nom_fond', models.CharField(blank=True, max_length=25, null=True)),
                ('montant', models.IntegerField()),
                ('objectif', models.CharField(blank=True, max_length=100, null=True)),
                ('id_membre', models.ForeignKey(db_column='id_membre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_tontine', models.ForeignKey(db_column='id_tontine', on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine')),
            ],
            options={
                'db_table': 'Fond',
            },
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id_election', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('heure_election', models.TimeField()),
                ('temps_renouvelable', models.IntegerField()),
                ('id_tontine', models.ForeignKey(db_column='id_tontine', on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine')),
            ],
            options={
                'db_table': 'Election',
            },
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('id_cotisation', models.AutoField(primary_key=True, serialize=False)),
                ('nom_cotisation', models.CharField(max_length=25)),
                ('montant', models.IntegerField()),
                ('date_debut', models.DateField()),
                ('cycle', models.IntegerField()),
                ('nb_participant', models.IntegerField()),
                ('taux_interet', models.IntegerField()),
                ('id_tontine', models.ForeignKey(db_column='id_tontine', on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine')),
            ],
            options={
                'db_table': 'Cotisation',
            },
        ),
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id_candidat', models.AutoField(primary_key=True, serialize=False)),
                ('id_election', models.ForeignKey(db_column='id_election', on_delete=django.db.models.deletion.CASCADE, to='tontine.election')),
                ('id_membre', models.ForeignKey(db_column='id_membre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_poste', models.ForeignKey(db_column='id_poste', on_delete=django.db.models.deletion.CASCADE, to='tontine.poste')),
            ],
            options={
                'db_table': 'Candidat',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_candidat', models.ForeignKey(db_column='id_candidat', on_delete=django.db.models.deletion.CASCADE, to='tontine.candidat')),
                ('id_election', models.ForeignKey(db_column='id_election', on_delete=django.db.models.deletion.CASCADE, to='tontine.election')),
                ('id_membre', models.ForeignKey(db_column='id_membre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_poste', models.ForeignKey(db_column='id_poste', on_delete=django.db.models.deletion.CASCADE, to='tontine.poste')),
            ],
            options={
                'db_table': 'Vote',
                'unique_together': {('id_membre', 'id_election', 'id_poste')},
            },
        ),
        migrations.CreateModel(
            name='ParticipantReunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_membre', models.ForeignKey(db_column='id_membre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_reunion', models.ForeignKey(db_column='id_reunion', on_delete=django.db.models.deletion.CASCADE, to='tontine.reunion')),
            ],
            options={
                'db_table': 'Participant_Reunion',
                'unique_together': {('id_reunion', 'id_membre')},
            },
        ),
        migrations.CreateModel(
            name='Cotiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('id_cotisation', models.ForeignKey(db_column='id_cotisation', on_delete=django.db.models.deletion.CASCADE, to='tontine.cotisation')),
                ('id_membre', models.ForeignKey(db_column='id_membre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cotiser',
                'unique_together': {('id_membre', 'id_cotisation', 'date')},
            },
        ),
        migrations.CreateModel(
            name='ContribuerFond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('id_fond', models.ForeignKey(db_column='id_fond', on_delete=django.db.models.deletion.CASCADE, to='tontine.fond')),
                ('id_membre', models.ForeignKey(db_column='id_membre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Contribuer_fond',
                'unique_together': {('id_fond', 'id_membre', 'date')},
            },
        ),
        migrations.CreateModel(
            name='AppartenirTontine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(blank=True, max_length=30, null=True)),
                ('nbr_parts', models.IntegerField()),
                ('id_membre', models.ForeignKey(db_column='id_membre', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_tontine', models.ForeignKey(db_column='id_tontine', on_delete=django.db.models.deletion.CASCADE, to='tontine.tontine')),
            ],
            options={
                'db_table': 'Appartenir_tontine',
                'unique_together': {('id_membre', 'id_tontine')},
            },
        ),
    ]
