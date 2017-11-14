from django.db import models

class Friend(models.Model):
		friend_name = models.CharField(max_length=400)
		npm = models.CharField(max_length=250)
		alamat = models.CharField(max_length=400, default="-")
		ttl = models.CharField(max_length=400, default="-")
		prodi = models.CharField(max_length=100, default="-")
		added_at = models.DateField(auto_now_add=True)