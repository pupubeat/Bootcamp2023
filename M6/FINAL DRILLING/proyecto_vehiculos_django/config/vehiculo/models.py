from django.db import models

class VehiculoModel(models.Model):

    MARCAS_CHOICES= (
        ('FIAT', 'Fiat'),
        ('CHEVROLET', 'Chevrolet'),
        ('FORD', 'Ford'),
        ('TOYOTA', 'Toyota'),
    )

    CATEGORIAS_CHOICES= (
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga'),
    )


    Marca = models.CharField(max_length=20, choices= MARCAS_CHOICES, default='Ford')
    Modelo = models.CharField(max_length=100)
    Serial_carroceria = models.CharField(max_length=50)
    Serial_motor = models.CharField(max_length=50)
    Particular = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES, default='Particular')
    Precio = models.FloatField()
    Fecha_creacion = models.DateField(auto_now_add=True)
    Fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.Marca

