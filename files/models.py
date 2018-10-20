import os
import uuid

from django.db import models


class DataFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='register/datafile/file')
    original_file_name = models.CharField(max_length=500, blank=True, null=True)
    extension = models.CharField(max_length=200, blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        filename, extension = os.path.splitext(self.file.name)
        self.original_file_name = os.path.basename(filename).strip()
        self.extension = extension.strip().lower()
        super().save(*args, **kwargs)


class Picture(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(
        upload_to='register/picture/image'
    )

    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return 'Picture #{id} ({title})'.format(
            id=self.id,
            title=self.title or 'Untitled'
        )
