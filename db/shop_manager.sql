DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;


CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  manufacturers_name VARCHAR(255),
  country_origin VARCHAR(255)
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  product_name VARCHAR(255),
  product_type VARCHAR(255),
  product_description TEXT,
  stock_quantity smallint,
  buying_cost money,
  selling_price money,
  product_manufacturer VARCHAR(255),
  product_image TEXT,
  manufacturer_id INT REFERENCES manufacturers(id)
);
