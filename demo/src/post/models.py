from django.db import models
from django.utils.encoding import smart_text


PRIVACY_TYPE = (
	("PR" , "Private"),
	("PB" , "Public"),
	)
# Create your models here.
class Post(models.Model):
	post_id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=100)
	content = models.TextField(null=True, blank=True)
	post_type = models.CharField(max_length=3, choices=PRIVACY_TYPE, default=PRIVACY_TYPE[0][0])

	class Meta:
		db_table = "post_table"

	def __str__(self):
		return smart_text(self.post_id)