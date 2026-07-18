# Industrial Career Week 2024 (SOKT & ETU)

![Career Week 2024 Banner](docs/career-week-2024-overview.png)

This web application was custom-built for the **Student Office of Career and Employment (SOKT)** at **Saint Petersburg Electrotechnical University (ETU "LETI")** to manage and coordinate **Industrial Career Week 2024**.

The project is a production-proven, relatively large-scale system that successfully processed and managed registrations and check-ins for **around 400 participants** during the event.

🎨 **Design Mockup:** There was no dedicated Figma design mockup for this project. Instead, the design, layout, and core functionality were heavily reused and adapted from the previous year's event. See the original [Career Week 2023 Repository](https://github.com/matvej-melikhov/career-week-2023).

---

## Key Features

* **Participant Registration:** A public registration form with WTForms validation, dropdown selects, and data sanitation.
* **Local QR Code Generation:** On-the-fly ticket generation as QR codes directly on the backend server, eliminating external API dependencies.
* **Email Ticket Delivery:** Automatic email notifications containing personalized invitations and QR ticket images.
* **Organizer Check-in Tools (for SOKT Staff):**
  * **Built-in QR Scanner:** A dedicated `/scanner` page using client-side camera access to scan ticket QR codes instantly.
  * **Visitor Verification & Logging:** An admin check-in page `/check` to instantly verify participant details and mark their attendance in real time.
* **Secure Admin Dashboard:** A protected administrative interface (`/admin/info`) secured with HTTP Basic Authentication to let staff view, filter, search, and export participant data.

---

## Technology Stack

### Backend
* **Python 3** & **Flask** (Core application framework)
* **Flask-SQLAlchemy** (Database ORM)
* **Flask-Admin** (Administrative dashboard)
* **Flask-Mail** (SMTP email delivery)
* **WTForms** (Form validation and parsing)
* **python-dotenv** (Environment variable management)
* **qrcode** & **Pillow** (Local QR ticket generation)

### Frontend
* **HTML5** & **Sass/SCSS**
* **Vanilla JavaScript** (ES6+)
* **html5-qrcode** (Camera scanner integration)
* **FontAwesome** (Icons)
