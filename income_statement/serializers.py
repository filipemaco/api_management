from rest_framework import serializers

from .models import IncomeStatement


class IncomeStatementSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id', 'name', 'profit', 'loss', 'date', 'user', 'description',
            'created_at', 'updated_at'
            )
        model = IncomeStatement
