from django.db import models
from roles.models import Role
class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='permissions')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'menu', 'action')

    def __str__(self):
        return f'{self.role.name} - {self.menu.name} - {self.action.name}'