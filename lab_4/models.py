from django.db import models

class Message(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=27)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
=======
	name = models.CharField(max_length=27)
	email = models.EmailField()
	message = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message
>>>>>>> db51b323b861f141bcde36ffbb8f8792ba697b2b
