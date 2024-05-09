--  creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER holberton.new_order
AFTER INSERT ON holberton.orders FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name
