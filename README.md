# 🛡️ HorusSight: AI-Powered Cybersecurity Intelligence Platform

**HorusSight** is an advanced, enterprise-grade security platform designed to bridge the gap between technical vulnerability detection and strategic business risk management. It combines a high-performance scanning engine with **Agentic AI** to provide actionable security intelligence.

---

## 🏗️ System Architecture

The platform is divided into two major integrated components:

### 1. The Command Center (Frontend & API Gateway)
- **Framework**: Next.js 15 (App Router)
- **Role**: Handles user interaction, real-time log visualization, dynamic security dashboards (using Recharts), and AI report generation.
- **API Bridge**: Acts as a secure gateway that spawns and communicates with the Python Scanning Engine.

### 2. The Tactical Engine (Scanning & Analysis)
- **Core**: Python 3.10+
- **Role**: Performs deep-packet inspection, tactical crawling, and multi-threaded vulnerability probing (SQLi, XSS, SSRF, etc.).
- **Intelligence**: Integrates the **EWABA (Expert Web-Application Brain Assistant)** engine powered by Google Gemini for context-aware risk assessment.

---

## 🚀 Key Features

- **Multi-Threaded Scanning**: Parallel execution of security modules for maximum infiltration speed.
- **EWABA AI Analysis**: Transforms raw technical vulnerabilities into professional reports with business impact, simplified analogies, and prioritized roadmaps.
- **Tactical Dashboard**: Real-time data visualization of threat vectors, attack surface mapping (Radar Charts), and vulnerability trends.
- **Live Terminal**: Real-time log streaming from the engine directly to the web interface.
- **Bilingual Interface**: Seamlessly switch between English and French.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React 19, TypeScript, Tailwind CSS 4, Framer Motion |
| **Data Viz** | Recharts (Pie, Area, and Radar charts) |
| **Backend API** | Next.js API Routes (Node.js) |
| **Scanning Engine** | Python 3.10+, Requests, BeautifulSoup4 |
| **AI / LLM** | Google Generative AI (Gemini Flash 2.0) |
| **Persistence** | SQLite (Scan history & results) |
| **Reporting** | jsPDF (Automated PDF Generation) |

---

## 📋 Prerequisites

Before setting up HorusSight, ensure your environment meets these requirements:

- **Node.js**: v18.17.0+
- **Python**: v3.10+
- **Browser**: Modern browser (Chrome/Edge recommended for animations)
- **API Key**: A valid **Google Gemini API Key** (for EWABA Intelligence features)

---

## ⚙️ Installation & Configuration

### 1. Clone the Project
```bash
git clone https://github.com/Donchaminade/HorusSight.git
cd HorusSight
```

### 2. Setup the Frontend (horussight folder)
```bash
cd horussight
npm install
```

### 3. Setup the Python Engine
Ensure you have the required Python libraries:
```bash
pip install requests beautifulsoup4 google-generativeai python-dotenv
```

### 4. Environment Variables
Create a `.env` file in the `horussight` directory with the following:
```env
# Required for AI Features
GEMINI_API_KEY="your_google_ai_studio_api_key"

# Secure Token Management
JWT_SECRET="any_long_random_string"
```

---

## 🚀 Launching the Platform

1.  **Start the Web Interface**:
    ```bash
    cd horussight
    npm run dev
    ```
2.  **Access the Dashboard**:
    Open [http://localhost:3000](http://localhost:3000) in your browser.
3.  **Initiate a Scan**:
    Enter a target URL in the dashboard and monitor the **Live Terminal** as the engine begins its tactical analysis.

---

## 📂 Project Structure

```text
HorusSight/
├── horussight/             # Next.js Frontend & API
│   ├── app/                # App Router (Pages & API)
│   ├── components/         # UI Components (Monolithic App.tsx)
│   ├── lib/                # AI Services & Translations
│   ├── public/             # Static Assets
│   └── .env                # Configuration
├── engine/                 # Python Scanning Engine
│   ├── core/               # Orchestrator & Crawler
│   ├── modules/            # Vuln Detectors (SQLi, XSS, etc.)
│   └── ai/                 # EWABA AI Analyzer
└── README.md               # Master Documentation
```

---

## 📧 Contact & Contributions

-   **Lead Developer**: [Le_meneur Donchaminade](https://www.linkedin.com/in/chaminadeadjolou)
-   **Project Status**: Hackathon / Production-Candidate
-   **Website**:

---
*© 2026 HorusSight. Precision Security for the Digital Age.*
