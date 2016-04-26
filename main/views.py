from django.shortcuts import render

# Create your views here.


def list_view(request):
	context = {}
	type_of_search = request.GET.get('type', None)
	search_id = request.GET.get('id', None)
	appartments = []
	if type_of_search == 'gov':
		gov = Gov.objects.get(id=search_id)

		for area in gov.area_set.all():
			for appartment in area.appartment_set.all():
				appartments.append(appartment)

		context['appartments'] = appartments

	elif type_of_search == 'area':
		area = Area.object.get(id=search_id)
		for appartment in area.appartment_set.all():
			appartments.append(appartment)
		context['appartments'] = appartments
	return render(context, 'list_view.html', request)