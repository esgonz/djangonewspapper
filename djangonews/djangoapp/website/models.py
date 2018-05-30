from django.db import models

# Create your models here.


class NewsType(models.Model):
	type_name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)

class Category(models.Model):
	category = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)

class Author(models.Model):
	name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	email = models.EmailField()
	thumb = models.CharField(max_length = 300)

class Status(models.Model):
	status_name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)



class MediaType(models.Model):
	type_name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)

class Media(models.Model):
	media_url = models.CharField(max_length = 300)
	caption = models.CharField(max_length = 200)
	media_type = models.ForeignKey(MediaType, on_delete=models.DO_NOTHING)

class FeatureMedia(models.Model):
	media = models.ForeignKey(Media, on_delete=models.DO_NOTHING)

class News(models.Model):
	epigraph = models.TextField()
	title = models.TextField()
	subhead = models.TextField()
	copy = models.TextField()
	news_type = models.ForeignKey(NewsType, on_delete=models.DO_NOTHING)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
	slug = models.CharField(max_length=100)
	author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	date = models.DateTimeField()
	status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
	feature_media = models.ForeignKey(FeatureMedia, on_delete=models.DO_NOTHING)
	created = models.DateTimeField()
	modified = models.DateTimeField(auto_now=True)
	deleted = models.DateTimeField()

class Tags(models.Model):
	tag = models.CharField(max_length = 60)

class NewsTags(models.Model):
	news = models.ForeignKey(News, on_delete=models.DO_NOTHING)
	tag = models.ForeignKey(Tags, on_delete=models.DO_NOTHING)

class Gallery(models.Model):
	media = models.ForeignKey(Media, on_delete=models.DO_NOTHING)
	news = models.ForeignKey(News, on_delete=models.DO_NOTHING)
