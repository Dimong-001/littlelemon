from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Booking

import json
from django.shortcuts import render
class ReservationsView(View):
    def get(self, request):
        date = request.GET.get('date')
        if date:
            bookings = Booking.objects.filter(reservation_date=date).values()
            return JsonResponse(list(bookings), safe=False)
        else:
            return JsonResponse([], safe=False)

    @method_decorator(csrf_exempt)
    def post(self, request):
        data = json.loads(request.body)
        try:
            Booking.objects.create(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot']
            )
            return JsonResponse({'message': 'Reservation created'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


def home(request):
    return render(request, 'restaurant/booking.html')

# Compare this snippet from littlelemon/restaurant/views.py:
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class BookingListView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            first_name = data.get('first_name')
            reservation_date = data.get('reservation_date')
            reservation_slot = data.get('reservation_slot')

            if not (first_name and reservation_date and reservation_slot):
                return JsonResponse({'error': 'All fields are required'}, status=400)

            if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
                return JsonResponse({'error': 'This slot is already booked!'}, status=400)

            booking = Booking.objects.create(
                first_name=first_name,
                reservation_date=reservation_date,
                reservation_slot=reservation_slot
            )

            return JsonResponse({
                'message': 'Booking created successfully',
                'booking_id': booking.id
            }, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
def post(self, request):
    try:
        print(request.body)  # Debug incoming data
        data = json.loads(request.body)
        print('Received data:', data)

        first_name = data.get('first_name')
        reservation_date = data.get('reservation_date')
        reservation_slot = data.get('reservation_slot')

        # Check for missing fields
        if not (first_name and reservation_date and reservation_slot):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        # Check for duplicate reservation
        if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
            return JsonResponse({'error': 'This slot is already booked!'}, status=400)

        # Create booking
        booking = Booking.objects.create(
            first_name=first_name,
            reservation_date=reservation_date,
            reservation_slot=reservation_slot
        )

        return JsonResponse({
            'message': 'Booking created successfully',
            'booking_id': booking.id
        }, status=201)

    except Exception as e:
        print(f'ERROR: {e}')  # Debug error
        return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class BookingListView(View):
    def get(self, request):
        date = request.GET.get('date')
        if date:
            bookings = Booking.objects.filter(reservation_date=date).values()
            return JsonResponse(list(bookings), safe=False)
        else:
            return JsonResponse({'error': 'Date parameter is required'}, status=400)

    def post(self, request):
        import json
        data = json.loads(request.body)
        first_name = data.get('first_name')
        reservation_date = data.get('reservation_date')
        reservation_slot = data.get('reservation_slot')

        if not all([first_name, reservation_date, reservation_slot]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
            return JsonResponse({'error': 'This slot is already booked!'}, status=400)

        booking = Booking.objects.create(
            first_name=first_name,
            reservation_date=reservation_date,
            reservation_slot=reservation_slot
        )

        return JsonResponse({'message': 'Booking created successfully'}, status=201)