##🎨 Style Guide to the Dashboard

1️⃣ Colors

| Color Usage | Hex Code | Purpose |
|----------|----------|----------|
| Primary | #FFFFFF (White) | Backgrounds, cards, and main layout |
| Secondary | #5A67BA (Purple) | Call-to-action buttons, active links, and highlights |
| Tertiary | #000000 (Black) | Text, icons, and key UI elements for contrast |

2️⃣ ##Typography

📌 Font Choices

Primary Font: Inter

Alternative Font: Poppins

🔤 ##Font Weights

700 (Bold) → Headings

500 (Medium) → Subheadings

400 (Regular) → Body text

🔲 ßInput Fields

border: 1px solid #5A67BA;
padding: 10px;ß
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


##Deployment Process
###Cloud Deployment (For Production)

For the frontend, I'll host it on Vercel because it's super easy to integrate with GitHub, and it automatically rebuilds and redeploys whenever I push changes. It also gives me a free domain and SSL for security.
For the backend, I'll use Render or Railway, which are great for hosting Node.js applications with a free tier. I'll push my backend code to GitHub, connect it to Render, and deploy it from there. The API will then be publicly accessible, and my frontend can easily communicate with it.

For the database, I'll go with MySQL and use PlanetScale, Railway, or Supabase—all of these offer managed databases, so I don’t have to worry about setup and maintenance. I’ll just connect my backend to one of these services, run my migrations, and I’m good to go.

###Local Deployment (For Development)

During development, I’ll run everything locally. The frontend will be a React app, which I can start with:


``` npm start ```


The backend will run using:


``` npm run dev ```


And for the database, I can either install MySQL locally or use Docker to spin up a MySQL instance like this:


``` docker run --name food-db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=food_tracker -p 3306:3306 -d mysql ```


After, I'll run my database migrations to set up the necessary tables.


Infrastructure Overview
Frontend: React (Hosted on Vercel)
Backend: Node.js + Express (Hosted on Rendßer/Railway)
Database: MySQL (Managed via PlanetScale, Railway, or Supabase)
CI/CD: I could use GitHub Actions for automated testing and deployment
Authentication: Firebase/Auth0

[GitHub Repo](https://github.com/TetaDory/Kurikirana)
[Prototype](https://www.figma.com/proto/feFOP4qByQMAJOpTDF4Rs1/Kurikirana?node-id=207-245&t=a1yMzvtXU78GJiOL-1)