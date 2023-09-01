from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    
    def __str__(self) :
        return self.name
    class Meta:
        db_table= 'Tipo'
        verbose_name= 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering= ['id']

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    
    def __str__(self) :
        return self.name
    class Meta:
        db_table= 'Categoria'
        verbose_name= 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering= ['id']    

class Employee(models.Model):
    categoria = models.ManyToManyField(Category)
    type =models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=250, verbose_name='Nombres')
    dni = models.CharField(max_length=25, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_created= models.DateTimeField(auto_now=True)
    date_updated= models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=000, max_digits=9, decimal_places=0)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    evitae = models.FileField(upload_to='evitae/%Y/%m/%d', null=True, blank=True)


    def __str__(self) :
        return self.names
    class Meta:
        db_table= 'Empleado'
        verbose_name= 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering= ['id']

    


    
    