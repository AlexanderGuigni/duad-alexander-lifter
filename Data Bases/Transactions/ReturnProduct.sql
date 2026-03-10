DO $$
DECLARE
    v_user_id INT := 1; -- ID user
    v_product_id INT := 2; -- ID product
    v_quantity INT := 1; -- Quantity of the product to return
    v_price DECIMAL(10, 2); -- Product price
    v_total DECIMAL(10, 2); -- Total return amount
    v_stock INT; -- Available product stock
    v_invoice_id INT; -- Invoice ID
BEGIN
    --Check the invoice exists
    IF NOT EXISTS (SELECT 1 FROM Invoices WHERE id = v_invoice_id) THEN
        RAISE EXCEPTION 'Invoice with ID % does not exist', v_invoice_id;
    END IF;
    --Increase the product stock
    UPDATE Products SET stock = stock + v_quantity WHERE id = v_product_id;
    --Update invoice as returned
    UPDATE Invoices SET is_returned = TRUE WHERE id = v_invoice_id;
END $$;