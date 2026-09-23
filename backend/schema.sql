-- KrishiSetu AI Relational Database Schema Setup
-- Database Management System: PostgreSQL

-- 1. Table to store master farmer registry profiles
CREATE TABLE IF NOT EXISTS farmers (
    farmer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    village_name VARCHAR(100),
    district VARCHAR(50) DEFAULT 'Nellore',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Table to list regional government market facility units (Mandis)
CREATE TABLE IF NOT EXISTS mandis (
    mandi_id SERIAL PRIMARY KEY,
    mandi_name VARCHAR(100) NOT NULL,
    max_truck_capacity INT NOT NULL,
    current_occupancy_count INT DEFAULT 0
);

-- 3. Table to track individual crop scan records and automated AI evaluations
CREATE TABLE IF NOT EXISTS crop_scans (
    scan_id SERIAL PRIMARY KEY,
    farmer_id INT REFERENCES farmers(farmer_id) ON DELETE CASCADE,
    crop_type VARCHAR(50) NOT NULL,
    ai_calculated_grade CHAR(1) NOT NULL, -- 'A' for Premium, 'B' for Standard, etc.
    confidence_score DECIMAL(5,2),        -- e.g. 94.50% confidence from AI model
    scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Table to handle token slot management for orderly market entries
CREATE TABLE IF NOT EXISTS mandi_appointments (
    token_id VARCHAR(30) PRIMARY KEY, -- e.g., TOKEN-SIH-4321
    farmer_id INT REFERENCES farmers(farmer_id),
    mandi_id INT REFERENCES mandis(mandi_id),
    scheduled_slot TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'Scheduled', -- Scheduled, Completed, Cancelled
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert starting sample data parameters for testing local setups
INSERT INTO mandis (mandi_name, max_truck_capacity, current_occupancy_count) VALUES
('Nellore Main Mandi Hub', 100, 42),
('Kavali Procurement Center', 50, 44),
('Gudur Agricultural Yard', 80, 12);
