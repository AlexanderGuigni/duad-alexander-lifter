DO $$
DECLARE
    v_user_id INT := 1; -- ID user
    v_product_id INT := 2; -- ID product
    v_quantity INT := 3; -- Quantity of the product to buy
    v_price DECIMAL(10, 2); -- Product price
    v_total DECIMAL(10, 2); -- Total purchase amount
    v_stock INT; -- Available product stock
BEGIN
    --Check stock
    SELECT price, stock INTO v_price, v_stock FROM Products WHERE id = v_product_id;
    IF v_stock < v_quantity THEN
        RAISE EXCEPTION 'There is not enough stock for the product with ID %', v_product_id;
    END IF;
    --Check user
    IF NOT EXISTS (SELECT 1 FROM Users WHERE id = v_user_id) THEN
        RAISE EXCEPTION 'User with ID % does not exist', v_user_id;
    END IF;
    --Create invoice
    v_total := v_price * v_quantity;
    INSERT INTO Invoices (user_id, total) VALUES (v_user_id, v_total) RETURNING id INTO v_invoice_id;
    --Update stock
    UPDATE Products SET stock = stock - v_quantity WHERE id = v_product_id;
    --Create invoice details
    INSERT INTO InvoiceDetails (invoice_id, product_id, quantity, price) VALUES (v_invoice_id, v_product_id, v_quantity, v_price);
END $$;