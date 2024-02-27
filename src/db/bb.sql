
\connect products
CREATE TABLE brands (
    brand_id INTEGER PRIMARY KEY,
    brand_name VARCHAR(255) NOT NULL
);


-- COPY brands
-- FROM '/datasets/brands.csv'
-- DELIMITER ','
-- CSV HEADER;