-- 1. b) i) this finds out how much customer GR01932 spent on flight GH182
select forename, surname, ((adultTicket * 5.50) + (childTicket * 2.00) + (concessionTicket * 1.50)) as "Tax(£)"
from customer, booking, flight
where customer.customerID = booking.customerID
and booking.flightID = flight.flightID 
and customer.customerID like "GR01932"
and flight.flightID like "QH182";

-- 1. b) ii) this finds the customers who have made a booking with the largest ammount of children 
select forename, surname
from customer, booking
where customer.customerID = booking.customerID 
and booking.childTicket = (select max(childTicket) from booking);

