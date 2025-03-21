-- Table: Farmers
CREATE TABLE Farmers (
    farmer_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(255),
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE
);

-- Table: Soil
CREATE TABLE Soil (
    soil_id INT IDENTITY(1,1) PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    moisture_level FLOAT,
    pH_level FLOAT,
    nitrogen FLOAT,
    phosphorus FLOAT,
    potassium FLOAT
);

-- Table: Crops
CREATE TABLE Crops (
    crop_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    suitable_soil_id INT REFERENCES Soil(soil_id),
    water_requirement FLOAT,
    temperature_range VARCHAR(50)
);

-- Table: Weather Data
CREATE TABLE Weather (
    weather_id INT IDENTITY(1,1) PRIMARY KEY,
    location VARCHAR(255) NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    rainfall FLOAT,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table: Recommendations
CREATE TABLE Recommendations (
    recommendation_id INT IDENTITY(1,1) PRIMARY KEY,
    farmer_id INT REFERENCES Farmers(farmer_id),
    soil_id INT REFERENCES Soil(soil_id),
    crop_id INT REFERENCES Crops(crop_id),
    recommendation_text TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table: Smart Irrigation
CREATE TABLE SmartIrrigation (
    irrigation_id INT IDENTITY(1,1) PRIMARY KEY,
    farmer_id INT REFERENCES Farmers(farmer_id),
    soil_id INT REFERENCES Soil(soil_id),
    weather_id INT REFERENCES Weather(weather_id),
    irrigation_status VARCHAR(50),
    water_used FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);