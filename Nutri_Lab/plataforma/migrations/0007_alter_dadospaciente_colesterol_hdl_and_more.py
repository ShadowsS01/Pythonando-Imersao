# Generated by Django 4.0.6 on 2022-07-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "plataforma",
            "0006_alter_refeicao_carboidratos_alter_refeicao_gorduras_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="dadospaciente",
            name="colesterol_hdl",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="dadospaciente",
            name="colesterol_ldl",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="dadospaciente",
            name="colesterol_total",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="dadospaciente",
            name="percentual_gordura",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="dadospaciente",
            name="percentual_musculo",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="dadospaciente",
            name="peso",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="dadospaciente",
            name="trigliceridios",
            field=models.FloatField(),
        ),
    ]