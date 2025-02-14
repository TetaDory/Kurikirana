🎨 Style Guide to the Dashboard

1️⃣ Colors

| Color Usage | Hex Code | Purpose |
|----------|----------|----------|
| Primary | #FFFFFF (White) | Backgrounds, cards, and main layout |
| Secondary | #5A67BA (Purple) | Call-to-action buttons, active links, and highlights |
| Tertiary | #000000 (Black) | Text, icons, and key UI elements for contrast |






Purpose

Primary

#FFFFFF (White)

Backgrounds, cards, and main layout

Secondary

#5A67BA (Muted Blue)

Call-to-action buttons, active links, and highlights

Tertiary

#000000 (Black)

Text, icons, and key UI elements for contrast

💡 Usage:

White (#FFFFFF) → Backgrounds, cards, and main layout.

Blue (#5A67BA) → Call-to-action buttons, active links, and highlights.

Black (#000000) → Text, icons, and key UI elements.

2️⃣ Typography

📌 Font Choices

Primary Font: Inter (Modern & versatile)

Alternative Font: Poppins (Sleek & professional)

🔤 Font Weights

700 (Bold) → Headings

500 (Medium) → Subheadings

400 (Regular) → Body text

3️⃣ Buttons & Inputs

🔘 Button Styles

Button Type

Background

Text Color

Border

Primary

#5A67BA (Muted Blue)

#FFFFFF (White)

None

Secondary

Transparent

#5A67BA (Muted Blue)

2px solid #5A67BA

Disabled

#A0AEC0 (Muted Gray)

#FFFFFF (White)

None

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
