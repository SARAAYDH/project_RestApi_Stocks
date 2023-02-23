from rest_framework import serializers
from .models import stock

class stockserilzers(serializers.ModelSerializer):
	class Meta:
		model=stock
		fields=('ticker','volume')