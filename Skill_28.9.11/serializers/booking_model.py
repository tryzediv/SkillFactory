from pydantic import BaseModel, Field


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingResponseModel(BaseModel):
    first_name: str = Field(..., description="Firstname for the guest who made the booking")
    last_name: str = Field(..., description="Lastname for the guest who made the booking")
    total_price: int = Field(..., description="The total price for the booking")
    deposit_paid: bool = Field(..., description="Whether the deposit has been paid or not")
    booking_dates: dict = Field(..., description="Sub-object that contains the checkin and checkout dates")
    additional_needs: str = Field(None, description="Any other needs the guest has")

    class Config:
        allow_population_by_field_name = True


class CreateBookingRequest(BaseModel):
    first_name: str = Field(..., description="Firstname for the guest who made the booking")
    last_name: str = Field(..., description="Lastname for the guest who made the booking")
    total_price: int = Field(..., description="The total price for the booking")
    deposit_paid: bool = Field(..., description="Whether the deposit has been paid or not")
    booking_dates: BookingDates = Field(..., description="Dates for check-in and check-out")
    additional_needs: str = Field(..., description="Any other needs the guest has")


class BookingResponse(BaseModel):
    booking_id: int
    booking: CreateBookingRequest


class Booking(BaseModel):
    first_name: str
    last_name: str
    total_price: int
    deposit_paid: bool
    booking_dates: BookingDates
    additional_needs: str


class CreateBookingResponse(BaseModel):
    booking_id: int
