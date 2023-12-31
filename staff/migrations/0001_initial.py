# Generated by Django 4.2.7 on 2023-11-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff_Details",
            fields=[
                (
                    "employee_id",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=20)),
                ("department", models.CharField(max_length=5)),
                ("designation", models.CharField(max_length=20, null=True)),
                ("cl1_bal", models.IntegerField(null=True)),
                ("cl2_bal", models.IntegerField(null=True)),
                ("ML_bal", models.IntegerField(null=True)),
                ("VL_bal", models.IntegerField(null=True)),
                ("DL_bal", models.IntegerField(null=True)),
                ("LoP", models.IntegerField(null=True)),
                ("comp_off", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Statud_Leave_Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("department", models.CharField(max_length=5)),
                ("nature_of_leave", models.CharField(max_length=20)),
                ("no_of_days", models.IntegerField(null=True)),
                ("leave_from", models.DateField()),
                ("reason", models.CharField(max_length=200)),
                ("alt_class_sem", models.CharField(max_length=10)),
                ("alt_hour", models.IntegerField()),
                ("alt_subject", models.CharField(max_length=30)),
                ("alt_assigned_teacher", models.CharField(max_length=20)),
                ("alt_linways_assigned", models.CharField(max_length=5)),
                ("status_of_request", models.CharField(default="", max_length=10)),
                ("time_of_request", models.DateTimeField(null=True)),
                (
                    "aemployee_id",
                    models.ForeignKey(
                        max_length=15,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emp_id2",
                        to="staff.staff_details",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Leave_Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("department", models.CharField(max_length=5)),
                ("nature_of_leave", models.CharField(max_length=20)),
                ("no_of_days", models.IntegerField(null=True)),
                ("leave_from", models.DateField()),
                ("reason", models.CharField(max_length=200)),
                ("alt_class_sem", models.CharField(max_length=10)),
                ("alt_hour", models.IntegerField()),
                ("alt_subject", models.CharField(max_length=30)),
                ("alt_assigned_teacher", models.CharField(max_length=20)),
                ("alt_linways_assigned", models.CharField(max_length=5)),
                (
                    "status_of_request",
                    models.CharField(default="PENDING", max_length=10),
                ),
                ("time_of_request", models.DateTimeField(null=True)),
                (
                    "bemployee_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emp_id",
                        to="staff.staff_details",
                    ),
                ),
            ],
        ),
    ]
