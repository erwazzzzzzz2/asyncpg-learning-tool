\connect products

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    brand_id INTEGER NOT NULL,
            FOREIGN KEY (brand_id)
            REFERENCES brands (brand_id)
            ON UPDATE CASCADE ON DELETE CASCADE
)

-- COPY products
-- FROM '/datasets/products.csv'
-- DELIMITER ','
-- CSV HEADER;