select gnomeName, sum(quantity) as [total gnomes sold]
from gnome, gnomepurchase
where gnome.gnomeID = gnomePurchase.gnomeID and description like "solar"
group by gnomeid
order by sum(quantity) desc;

select max(unitprice) as [expensive]
from gnome;
select emailAddress, orderID, Quantity
from customer, custOrder, gnomePurchase, gnome, maxgnomeprice
where customer.customerID = custOrder.customerID 
and custOrder.orderID = gnomepurchase.orderID 
and gnome.gnomeID = gnomepurchse.gnomeID 
and unitprice = [expensive] and quantity >= 3;

select forename, surname (quantity * unitprice * 1.2) as [total to pay £]
from customer, gnome, gnomepurchase, custorder 
where custorder.orderID = 'ord0024'
and customer.customer.ID = custorder.customerID
and custorder.orderID = gnomepurchase.orderID
and gnome.gnomeID = gnomepurchase.gnomeID
group by forename, surname

