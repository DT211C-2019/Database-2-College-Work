-- A
select stock_code, stock_description 
from b2_stock 
where unit_price < unitcostprice;

-- B
select stock_code, stock_description 
from b2_stock 
where stock_level < reorder_level;

-- C
select b2_customer.customer_name, b2_customer.customer_id
from b2_customer
left join b2_corder 
on b2_customer.customer_id=b2_corder.customer_id
where b2_corder.customer_id is null;

-- D
SELECT b2_customer.customer_name, b2_stock.stock_description
FROM b2_customer, b2_corder, b2_corderline, b2_stock
WHERE b2_customer.customer_id=b2_corder.customer_id
AND b2_corder.corderno=b2_corderline.corderno
AND b2_corderline.stock_code=b2_stock.stock_code
AND b2_customer.customer_name='John Flaherty';

--E
select supplier_name
from b2_supplier
left join b2_sorder
on b2_sorder.supplier_id=b2_supplier.supplier_id
where b2_sorder.sorderno=Null;

-- F
select b2_corder.customer_id, b2_stock.stock_code
from b2_corder, b2_corderline, b2_stock
where b2_corder.corderno=b2_corderline.corderno
and b2_corderline.stock_code=b2_stock.stock_code
and b2_stock.stock_code='A101' or b2_stock.stock_code='A111';

-- G
select b2_staff.staff_name, b2_customer.customer_name
from b2_customer, b2_corder, b2_staff
where b2_customer.customer_id=b2_corder.customer_id
and b2_corder.staffpaid=b2_staff.staff_no
and b2_corder.staffpaid='Mary Martin';
