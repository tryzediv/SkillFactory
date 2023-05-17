import pytest
import requests
from pydantic import ValidationError
from serializers.booking_model import BookingResponseModel, CreateBookingRequest, BookingResponse


@pytest.mark.without_token
@pytest.mark.parametrize('booking_id, expected_status, headers', [
    (1, 200, {"Accept": "application/json"}),
    (0, 404, {"Accept": "application/json"}),
    (-1, 404, {"Accept": "application/json"}),
    ('a', 404, {"Accept": "application/json"}),
    (1, 418, {"Accept": ""}),
    (1, 200, None)])
def test_get_booking(booking_id, expected_status, headers):
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"

    response = requests.get(url, headers=headers)

    assert response.status_code == expected_status, f"Request failed with status code {response.status_code}"

    if expected_status == 200:
        try:
            data = response.json()
            booking = BookingResponseModel(**data)
        except (ValidationError, TypeError) as e:
            pytest.fail(f"Failed to validate booking response data: {e}")

        assert booking.first_name != '', "Firstname is missing"
        assert booking.last_name != '', "Lastname is missing"
        assert booking.total_price >= 0, "Total price must be non-negative"
        assert isinstance(booking.deposit_paid, bool), "Depositpaid must be a boolean"
        assert isinstance(booking.booking_dates, dict), "Bookingdates must be a dictionary"
        assert "checkin" in booking.booking_dates and isinstance(booking.booking_dates["checkin"], str), \
            "Checkin date is missing or invalid"
        assert "checkout" in booking.booking_dates and isinstance(booking.booking_dates["checkout"], str), \
            "Checkout date is missing or invalid"


@pytest.mark.xfail
@pytest.mark.without_token
@pytest.mark.parametrize('headers, request_body, expected_status', [
    ({"Content-Type": "application/json", "Accept": "application/json"},
     {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
        "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
        "additionalneeds": "Breakfast"}, 200),          # Valid data positive test
    ({"Content-Type": "text/plain", "Accept": "text/plain"},
     {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
      "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
        "additionalneeds": "Breakfast"}, 415),          # Invalid headers negative test BUG HERE
    (None, {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
        "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
        "additionalneeds": "Breakfast"}, 200)])         # No headers negative test
def test_create_booking(headers, request_body, expected_status):
    url = "https://restful-booker.herokuapp.com/booking"

    try:
        request_data = CreateBookingRequest(**request_body)
    except ValidationError as e:
        pytest.fail(f"Failed to validate request data: {e}")

    response = requests.post(url, headers=headers, json=request_data.dict())

    assert response.status_code == expected_status, f"Request failed with status code {response.status_code}"

    if expected_status == 200:
        try:
            response_data = response.json()
            booking_response = BookingResponse(**response_data)
        except (ValidationError, TypeError) as e:
            pytest.fail(f"Failed to validate booking response data: {e}")

        assert booking_response.booking_id is not None and isinstance(booking_response.booking_id, int), \
            "Booking ID is missing or invalid"
        assert isinstance(booking_response.booking, CreateBookingRequest), \
            "Booking data is missing or invalid"
        booking = booking_response.booking
        assert booking.first_name == request_data.first_name, "Invalid firstname in the response"
        assert booking.last_name == request_data.last_name, "Invalid lastname in the response"
        assert booking.total_price == request_data.total_price, "Invalid totalprice in the response"
        assert booking.deposit_paid == request_data.deposit_paid, "Invalid depositpaid in the response"
        assert booking.booking_dates.dict() == request_data.booking_dates.dict(), "Invalid bookingdates in the response"
        assert booking.additional_needs == request_data.additional_needs, "Invalid additionalneeds in the response"
