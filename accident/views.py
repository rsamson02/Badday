from badday.accident.models import Accident, AccidentType, VehicleType
from django.http import HttpResponse 
from django.shortcuts import render_to_response, get_object_or_404

def homepage(request):
    latest_accident_list = Accident.objects.all().order_by('-pub_date')[:5]
    accident_types = AccidentType.objects.order_by('accident_type')
    vehicle_types = VehicleType.objects.order_by('vehicle_type')
    return render_to_response('homepage.html', {
        'latest_accident_list': latest_accident_list,
        'accident_types': accident_types,
        'vehicle_types': vehicle_types
})

def detail(request, accident_id):
    crash = get_object_or_404(Accident, pk=accident_id)
    return render_to_response('detail.html', {'crash': crash})

    
def accident_typesdetail(request, accident_id):
    atype = get_object_or_404(AccidentType, pk=accident_id)
    crashes = Accident.objects.filter(accident_type=atype)
    return render_to_response('accidenttypesdetail.html', {'atype': atype, 'crashes': crashes})

def vehicle_typesdetail(request, vehicle_id):
    vtype = get_object_or_404(VehicleType, pk=vehicle_id)
    crashes = Accident.objects.filter(vehicle_type=vtype)
    return render_to_response('vehicletypesdetail.html', {'vtype': vtype, 'crashes': crashes})
