# 🛡️ HorusSight — Advanced Cybersecurity Scanning Platform

HorusSight is a premium, high-performance cybersecurity platform designed for automated vulnerability scanning, real-time threat intelligence, and AI-driven remediation analysis. It combines a robust Next.js frontend with a powerful multi-threaded Python scanning engine.

---

## 🚀 How It Works

HorusSight operates in four distinct phases to ensure comprehensive security coverage:

1.  **Tactical Infiltration (Crawling)**: The platform's crawler maps the target URL, identifying all accessible pages, forms, and input parameters.
2.  **Full Power Scanning**: A multi-threaded engine (running up to 15 parallel workers) probes identified entry points for critical vulnerabilities like SQLi, XSS, SSRF, Command Injection, and more.
3.  **EWABA Intelligence**: The raw scan findings are processed by the **EWABA (Expert Vulnerability Analysis & Business Assessment)** AI engine (powered by Google Gemini). It provides business impact analysis and prioritized remediation steps.
4.  **Reporting & Mitigation**: Detailed reports are generated, providing actionable patches and a strategic communication template for stakeholders.

---

## 🛠️ Technology Stack

### Frontend & API Gateway
- **Framework**: [Next.js 15](https://nextjs.org/) (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS 4 (Custom Design System with Glassmorphism)
- **Animations**: Framer Motion (Fluid transitions & parallax effects)
- **State Management**: React Context & Hooks
- **PDF Generation**: jsPDF

### Backend Engine (Python)
- **Core Orchestrator**: Python 3.10+
- **Concurrency**: `concurrent.futures` (ThreadPoolExecutor)
- **Database**: SQLite (Persistent storage for scan history)
- **AI Integration**: Google Generative AI (Gemini Pro/Flash)

---

## 📋 Prerequisites

Before launching HorusSight, ensure you have the following installed:

- **Node.js**: v18.17.0 or higher
- **npm**: v9.0.0 or higher
- **Python**: v3.10 or higher
- **Python Packages**:
  - `requests`
  - `beautifulsoup4`
  - `google-generativeai`
  - `python-dotenv`
- **Gemini API Key**: Obtainable from [Google AI Studio](https://aistudio.google.com/)

---

## ⚙️ Configuration

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Donchaminade/HorusSight.git
    cd HorusSight/horussight
    ```

2.  **Frontend Dependencies**:
    ```bash
    npm install
    ```

3.  **Python Engine Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables**:
    Create a `.env` file in the `horussight` directory:
    ```env
    # Required for AI Analysis
    GEMINI_API_KEY="your_actual_api_key_here"

    # For Secure Session Management
    JWT_SECRET="your_random_secure_secret"
    ```

---

## 🚀 Launching the Platform

### Development Mode
To start the Next.js frontend and the API gateway:
```bash
npm run dev
```
The platform will be available at [http://localhost:3000](http://localhost:3000).

### Running a Scan
1.  Navigate to the **Dashboard**.
2.  Enter a target URL (e.g., `http://example.com`).
3.  Click **Initiate Tactical Scan**.
4.  Monitor real-time progress in the **Live Terminal**.

---

## 📁 Project Structure

-   `/app`: Next.js App Router (Layouts and API routes).
-   `/components`: Premium UI components (Hero, Dashboard, Terminal).
-   `/engine`: The heart of the platform (Python).
    -   `/core`: Orchestrator and Crawler.
    -   `/modules`: Vulnerability detectors (SQLi, XSS, etc.).
    -   `/ai`: EWABA AI Analysis engine.
-   `/lib`: Core utilities (AI Service, Translations, Database bridge).
-   `/public`: Static assets and Service Workers.

---

## 🌐 Bilingual Support

HorusSight features a built-in "Zero-Dependency" translation system.
-   Toggle between **English** and **French** directly from the UI.
-   Language preferences are persisted in `localStorage`.
-   Translation dictionary located at `lib/translations.ts`.

---

## 📧 Support & Contact

-   **Developer**: [Le_meneur Donchaminade](https://www.linkedin.com/in/chaminadeadjolou)
-   **Email**: contact@horussight.io
-   **License**: Private / Proprietary

---
*© 2026 HorusSight. Precision Security for the Digital Age.*
