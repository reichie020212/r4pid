import math
from django.core.exceptions import ValidationError
from django.db import models


class Shape(models.Model):

    class Meta:
        abstract = True

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Triangle(Shape):
    base = models.FloatField()
    height = models.FloatField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(base__gt=0),
                name='base_gt_0',
            ),
            models.CheckConstraint(
                check=models.Q(height__gt=0),
                name='height_gt_0',
            ),
        ]

    def calculate_sides(self):
        return math.sqrt((self.base ** 2) + self.height ** 2)

    def calculate_area(self):
        return (self.base * self.height) / 2

    def calculate_perimeter(self):
        return (self.calculate_sides() * 2) + self.base


class Square(Shape):
    length = models.FloatField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(length__gt=0),
                name='length_gt_0',
            ),
        ]

    def calculate_area(self):
        return self.length ** 2

    def calculate_perimeter(self):
        return self.length * 4


class Rectangle(Shape):
    width = models.FloatField()
    length = models.FloatField()

    class Meta(Square.Meta):
        constraints = [
            models.CheckConstraint(
                check=models.Q(length__gt=0),
                name='length_gt_0',
            ),
            models.CheckConstraint(
                check=models.Q(width__gt=0),
                name='width_gt_0',
            ),
        ]

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Diamond(Shape):
    width = models.FloatField()
    length = models.FloatField()
    angle = models.FloatField()

    class Meta(Rectangle.Meta):
        constraints = [
            models.CheckConstraint(
                check=models.Q(length__gt=0),
                name='length_gt_0',
            ),
            models.CheckConstraint(
                check=models.Q(width__gt=0),
                name='width_gt_0',
            ),
            models.CheckConstraint(
                check=models.Q(angle__gt=0),
                name='angle_gt_0',
            ),
            models.CheckConstraint(
                check=models.Q(angle__lt=180),
                name='angle_lt_180',
            ),
        ]

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def clean(self):
        if self.angle == 90:
            raise ValidationError('Angle should not be equal to 90 since angle with a 90 degrees is a rectangle.')

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)
