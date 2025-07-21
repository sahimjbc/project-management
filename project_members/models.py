from django.db import models

class ProjectRole(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='project_members')
    role = models.ForeignKey(ProjectRole, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('project', 'user')
    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.role.name if self.role else 'No Role'})"