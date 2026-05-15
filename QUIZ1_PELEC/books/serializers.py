from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    - Converts Book instances to/from JSON
    - Validates all input data
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_rating(self, value):
        """Ensure rating is between 0.0 and 5.0"""
        if value < 0.0 or value > 5.0:
            raise serializers.ValidationError(
                "Rating must be between 0.0 and 5.0."
            )
        return value

    def validate_title(self, value):
        """Ensure title is not blank"""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value.strip()

    def validate_author(self, value):
        """Ensure author is not blank"""
        if not value.strip():
            raise serializers.ValidationError("Author cannot be blank.")
        return value.strip()