🎨 Style Guide for Your Dashboard

1️⃣ Colors
Primary Color (Background, main areas) → #FFFFFF (White)
Secondary Color (Buttons, highlights, accents) → #5A67BA (Muted blue)
Tertiary Color (Text, icons, key elements) → #000000 (Black)
💡 Usage:
White (#FFFFFF): Backgrounds, cards, and main layout.
Blue (#5A67BA): Call-to-action buttons, active links, and highlights.
Black (#000000): Text, icons, and key UI elements for contrast.

2️⃣ Typography
📌 Use a clean, readable font that complements the colors.
Primary Font: Inter (Modern & versatile)
Alternative Font: Poppins (Sleek & professional)
Font Weights:
700 (Bold) → Headings
500 (Medium) → Subheadings
400 (Regular) → Body text

3️⃣ Buttons & Inputs
🔘 Button Styles:
Primary Button: background: #5A67BA; color: #FFFFFF; (Blue with white text)
Secondary Button: border: 2px solid #5A67BA; color: #5A67BA; (Outlined blue)
Disabled Button: background: #A0AEC0; color: #FFFFFF; (Muted gray when inactive)

🔲 Input Fields:
border: 1px solid #5A67BA;
padding: 10px;
border-radius: 6px;
color: #000000;

#Database Schema

| Column   | Type     | Constraints  | Description  |
|----------|----------|--------------|--------------|
| id       | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each food item |
| name     | VARCHAR(255) | NOT NULL | Name of the food |
| category | VARCHAR(100) | NOT NULL | Category |
| expiry date | DATE | NOT NULL | Expiration date of the food |
| storage location | Row 2, Col 2 | Row 2, Col 3 | Expiration date of the food |
| temperature | Row 2, Col 2 | Row 2, Col 3 |
| humidity | Row 2, Col 2 | Row 2, Col 3 |
