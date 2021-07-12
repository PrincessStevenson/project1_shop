DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS products;

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  manufacturers_name VARCHAR(255),
  country_origin VARCHAR(255)
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  product_name VARCHAR(255),
  product_type VARCHAR(255),
  product_description VARCHAR(255),
  stock_quantity tinyint,
  buying_cost smallmoney,
  selling_price smallmoney,
  product_manufacturer VARCHAR(255),
  manufacturer_id INT REFERENCES manufacturers(id)
);
