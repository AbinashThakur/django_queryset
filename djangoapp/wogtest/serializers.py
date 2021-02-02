from .models import table1
from rest_framework import serializers 
 
class ReqSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = table1
        # fields = ('city')
        # fields = ('id',
        #           'city',
        #           # 'userid',
        #           # 'uploaded_time',
        #           'price',
        #           # 'year',
        #           # 'county_name',
        #           # 'state_code',
        #           # 'state_name')
        #           )
        fields = '__all__'

class apiRes2(serializers.ModelSerializer):
	class Meta:
		model = table1

		fields = ('city', 'price')