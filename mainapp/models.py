from django.db import models

TODO = 'Todo'
IN_PROGRESS = 'In progress'
DONE = 'Done'

STATUS = (
    (TODO, 'Todo'),
    (IN_PROGRESS, 'In progress'),
    (DONE, 'Done'),
    
)

class InnerTraid(models.Model):
    name = models.CharField(max_length=127)
    status = models.CharField(choices = STATUS, default=TODO, max_length=127)
    date_create = models.DateTimeField(null=True, blank=True)
    date_update = models.DateTimeField(null=True, blank=True)
    date_finished = models.DateTimeField(null=True, blank=True)