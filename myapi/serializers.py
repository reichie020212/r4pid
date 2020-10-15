from django.contrib.auth.models import User
from rest_framework import serializers
from myapi.models import Triangle
from myapi.models import Square
from myapi.models import Rectangle
from myapi.models import Diamond


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'confirm_password',
        ]

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.pop('confirm_password')

        errors = {}

        if User.objects.filter(username=username).exists():
            errors.update({'username': 'Username is already used.'})
        if not username.isalpha():
            errors.update({'username': 'Space and special characters are not allowed'})
        if len(username) < 4:
            errors.update(
                {'username': 'Username must have a length of 4 or more.'})
        if len(password) < 4:
            errors.update(
                {'password': 'Password must have a length of 4 or more.'})

        if password != confirm_password:
            errors.update({'confirm_password': 'Password and Confirm Password do not match.'})

        if errors:
            raise serializers.ValidationError(errors)

        return data


class TriangleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Triangle
        fields = '__all__'

    def validate(self, data):
        base = data.get('base')
        height = data.get('height')

        errors = {}

        if base < 0:
            errors.update({'base': 'Base should not be less than 0.'})
        if height < 0:
            errors.update({'height': 'Height should not be less than 0.'})

        if errors:
            raise serializers.ValidationError(errors)

        return data


class SquareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Square
        fields = '__all__'

    def validate(self, data):
        length = data.get('length')

        errors = {}

        if length < 0:
            errors.update({'length': 'Length should not be less than 0.'})

        if errors:
            raise serializers.ValidationError(errors)

        return data


class RectangleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rectangle
        fields = '__all__'

    def validate(self, data):
        width = data.get('width')
        length = data.get('length')

        errors = {}

        if width < 0:
            errors.update({'width': 'Width should not be less than 0.'})
        if length < 0:
            errors.update({'length': 'Length should not be less than 0.'})

        if errors:
            raise serializers.ValidationError(errors)

        return data


class DiamondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diamond
        fields = '__all__'

    def validate(self, data):
        width = data.get('width')
        length = data.get('length')
        angle = data.get('angle')

        errors = {}

        if width < 0:
            errors.update({'width': 'Width should not be less than 0.'})
        if length < 0:
            errors.update({'length': 'Length should not be less than 0.'})
        if not (0 < angle < 180):
            errors.update({'angle': 'Angle should be greater than 0 and less than 180.'})
        elif angle == 90:
            errors.update({'angle': 'Angle should not be equal to 90 since angle with a 90 degrees is a rectangle.'})

        if errors:
            raise serializers.ValidationError(errors)

        return data
