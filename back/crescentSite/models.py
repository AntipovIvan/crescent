from django.db import models


# class YourModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()
#     additional_field1 = models.BooleanField(default=False)
#     additional_field2 = models.DateField()
#     cover = models.ImageField(
#         upload_to="images/", default="images/Placeholder.png"
#     )


class NewsModel(models.Model):
    date = models.DateField(null=True)
    title = models.CharField(max_length=225)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
