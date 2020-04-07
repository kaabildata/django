from django.db import models

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 255)
    deleted = models.BooleanField()

    def __repr__ (self):
        return "Item [" + \
        "id=" + (str(self.id) if self.id is not None else "[None]") + \
        ", name=" + ((self.name if (self.name is not None) else "[None]") if self.name is not None else "[None]") + \
        ", deleted=" + (str(self.deleted) if self.deleted is not None else "[None]") + \
        "]"
