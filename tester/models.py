from django.db import models


class User(models.Model):
    u_id = models.CharField(primary_key=True, max_length=20)
    u_nickname = models.TextField()
    u_email = models.EmailField(unique=True)
    u_warn_count = models.IntegerField(default=0)
    penalty_date = models.DateField()

    class Meta:
        db_table = 'user_info'

    def __str__(self):
        return '%s/%s' % (self.u_nickname, self.u_email)


class Manager(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    m_tel = models.TextField()


class Room(models.Model):
    r_name = models.TextField()


class Review(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='writer', null=True)
    r_id = models.ForeignKey(Room, on_delete=models.SET_NULL, related_name='room', null=True)
    review = models.TextField()
