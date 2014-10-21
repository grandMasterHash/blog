from django.db import models
from django.contrib import auth

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	author = models.ForeignKey(auth.models.User)
	date = models.DateTimeField('date published')
	average_rating = models.IntegerField(null=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	author = models.CharField(max_length=50)
	comment = models.TextField()
	date = models.DateTimeField()
	post = models.ForeignKey(Post)

	def __unicode__(self):
		date = self.date.date()
		date = str(date)
		return "%s %s #%d"%(self.author, date, self.id)

class Rating(models.Model):
	post = models.ForeignKey(Post)
	value = models.IntegerField()
	rater = models.CharField(max_length=50)
