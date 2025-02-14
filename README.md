🎨 Style Guide to the Dashboard

1️⃣ Colors

| Color Usage | Hex Code | Purpose |
|----------|----------|----------|
| Primary | #FFFFFF (White) | Backgrounds, cards, and main layout |
| Secondary | #5A67BA (Purple) | Call-to-action buttons, active links, and highlights |
| Tertiary | #000000 (Black) | Text, icons, and key UI elements for contrast |

2️⃣ Typography

📌 Font Choices

Primary Font: Inter

Alternative Font: Poppins

🔤 Font Weights

700 (Bold) → Headings

500 (Medium) → Subheadings

400 (Regular) → Body text

🔲 Input Fields

border: 1px solid #5A67BA;
padding: 10px;
border-radius: 6px;
color: #000000;

📂 Database Schema

| Column   | Type     | Constraints  | Description  |
|----------|----------|--------------|--------------|
| id       | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each food item |
| name     | VARCHAR(255) | NOT NULL | Name of the food |
| category | VARCHAR(100) | NOT NULL | Category |
| expiry date | DATE | NOT NULL | Expiration date of the food |
| storage location | VARCHAR(100) | NULLABLE | Where it's stored |
| temperature | DECIMAL(5,2) | NULLABLE | Temperature (°C) |
| humidity | DECIMAL(5,2) | NULLABLE | Humidity level in storage(%) |
