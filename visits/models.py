from django.db import models


class visitor(models.Model):
    path = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    scheme = models.CharField(max_length=100)

    # headers
    headers = models.TextField()
    #end headers

    body = models.CharField(max_length=100)

    user = models.CharField(max_length=100)
    info = models.TextField()

    # COOKIES
    COOKIES = models.TextField()
    # end COOKIES

    METAdata = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.user + '  |  '+ self.time

    # class Meta:
    #     verbose_name_plural = "Categories"