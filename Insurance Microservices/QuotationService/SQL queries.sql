CREATE DATABASE quotation_db;
use quotation_db;

CREATE TABLE quotes ( id INT AUTO_INCREMENT PRIMARY KEY, user_id VARCHAR(50) NOT NULL, insurance_type ENUM('travel', 'health') NOT NULL, destination VARCHAR(100), start_date DATE, end_date DATE, age INT, pre_existing_conditions TEXT, coverage_amount DECIMAL(10, 2), calculated_premium DECIMAL(10, 2) NOT NULL, quote_expiry DATETIME, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

INSERT INTO quotes ( user_id, insurance_type, destination, start_date, end_date, age, pre_existing_conditions, coverage_amount, calculated_premium, quote_expiry ) VALUES ( 'user123', 'travel', 'France', '2025-06-01', '2025-06-10', NULL, NULL, 100000.00, 520.75, '2025-06-01 23:59:59' );

SELECT * from quotes;

DELETE from quotes where user_id='101';