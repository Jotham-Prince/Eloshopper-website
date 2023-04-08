
# the necessary imports
from django.db import models

# the Frequenlty asked questions and the terms and conditions
class FAQ(models.Model):
	heading = models.CharField(max_length=200)
	description = models.TextField()
	term_title = models.CharField(max_length=400, default="terms title")
	term_description = models.TextField(default="terms and conditions...")
	policy = models.CharField(max_length=400, default="policy footer")

	def __str__(self):
		return f"{self.heading}"

# the subscribers
class Subscribers(models.Model):
	email = models.EmailField(null=False, blank=False)
	# how the string should appear in the back end(plurals)
	class Meta:
		db_table = 'subscribers'
		verbose_name_plural = 'Subscribers'
	# how the string is saved in the backend
	def __str__(self):
		return f"New Subscriber for email: {self.email}"
