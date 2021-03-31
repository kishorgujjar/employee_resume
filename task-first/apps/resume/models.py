from django.db import models


class ResumeItem(models.Model):
    """
    A single resume item, representing a job and title held over a given period
    of time.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=127, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    company = models.CharField(max_length=127)
    designation = models.CharField(max_length=127, null=True, blank=True)
    photo = models.ImageField(upload_to="gallery", null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=2047, blank=True)

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.user.username,
                                          self.title,
                                          self.company,
                                          self.photo,
                                          self.start_date.isoformat())
