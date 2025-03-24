// Auto-select today's date and load bookings on page load
document.addEventListener('DOMContentLoaded', async () => {
    const dateInput = document.getElementById('reservation_date');
    dateInput.valueAsDate = new Date();

    // Load reservations for today's date
    await loadReservations(dateInput.value);
});

// Function to load reservations
const loadReservations = async (date) => {
    const response = await fetch(`/bookings/?date=${date}`);
    const data = await response.json();

    const reservationList = document.getElementById('reservationList');
    reservationList.innerHTML = ''; // Clear previous reservations

    // Update the "Bookings For" section with the selected date
    document.getElementById('currentDate').innerText = date;

    if (data.length === 0) {
        reservationList.innerHTML = '<li class="text-gray-500">No bookings available</li>';
    } else {
        data.forEach(booking => {
            reservationList.innerHTML += `
                <li class="border-b py-2 flex justify-between p-2 bg-white rounded shadow">
                    <span class="text-gray-700 font-medium">${booking.first_name}</span>
                    <span class="text-gray-500">${booking.reservation_slot}</span>
                </li>
            `;
        });
    }
};

// Update booking list when date changes
document.getElementById('reservation_date').addEventListener('change', async (event) => {
    await loadReservations(event.target.value);
});

// Handle form submission
document.getElementById('bookingForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const date = document.getElementById('reservation_date').value;
    const slot = document.getElementById('reservation_slot').value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send the data to the backend
    const response = await fetch('/bookings/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            first_name: name,
            reservation_date: date,
            reservation_slot: slot
        })
    });

    if (response.ok) {
        alert('Reservation added successfully');
        await loadReservations(date); // Reload the list after adding a booking
    } else {
        const errorData = await response.json();
        alert(`Error adding reservation: ${errorData.error}`);
    }
});

// Mobile menu toggle
document.getElementById('mobile-menu-button').addEventListener('click', () => {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
});


