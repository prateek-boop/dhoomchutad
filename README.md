# EduEagle: Student Success and Intervention Orchestration Engine

Reference Platform: **EduEagle**  
Local Prototype Server: **http://localhost:8000**  
Local Network Mobile Access: **http://192.168.31.150:8000**

---

## Overview and Mission

Higher education institutions routinely accumulate rich attendance records, examination marks, fee balances, LMS telemetry, and faculty feedback, yet rarely convert these early indicators into **timely, empathetic, and trackable support**.

**EduEagle is an intervention layer that bridges insight to responsible action.**

### What EduEagle IS:
- A **Consent-Aware 360-Degree Student Success View** fusing 6 core pillars.
- An **Explainable Early-Risk Diagnostic Engine** that breaks down why a student needs attention with percentage driver attributions.
- A **Multi-Role Intervention Orchestration Engine** mapping signals to targeted workflows (Remedial support, Mentor assignment, Parent conference, Wellbeing referral, Fee support, Placement readiness).
- An **Accountable Stakeholder Dispatcher** with SLA deadlines and automatic escalation up the administrative hierarchy (Faculty -> HOD -> Dean).
- A **Closed-Loop Outcome and Proof Center** requiring auditable evidence of follow-up before recalculating risk.
- A **Student-Facing Self-Service Hub (Beacon)** providing academic transparency, personal support circles, emergency help requests, and privacy consent controls.

### What EduEagle is NOT:
- Not a passive attendance tracker.
- Not a generic conversational chatbot.
- Not just a dropout prediction score.

---

## Three Foundational Ethical AI Safeguards

| Safeguard | Implementation and Guarantee |
|---|---|
| **Anti-Punishment Policy** | Algorithmic risk scores are strictly prohibited from triggering automated exam bans, course de-registration, or punitive actions. Every flag triggers an offer of help, never a penalty. |
| **Non-Diagnostic Terminology Shield** | The engine strictly forbids psychiatric or medical diagnostic labelling (e.g. depression, ADHD, anxiety). All wellbeing alerts use behavioral, supportive language such as *"Academic fatigue"* or *"Confidential wellness check-in"*. |
| **Mandatory Human-in-the-Loop Override** | Any student, faculty member, or advisor can manually override algorithmic scores. Every override requires an auditable justification (min 10 characters) preserved permanently in the ledger. |

---

## Key Features

### 1. 360-Degree Holistic Success View (6 Pillars)
1. **Academic Performance and Trajectory**: Continuous Internal Evaluations (CIE), mid-term scores, course credits, and grade trajectory.
2. **Attendance Velocity and LMS Telemetry**: Overall % vs 30-day velocity, consecutive morning lecture absences, and LMS login gaps.
3. **Financial Wellness**: Fee balance, overdue days, scholarship eligibility, and emergency installment plan status.
4. **Skills and Career Readiness**: Campus mock interview scores, coding practice velocity, and capstone project milestones.
5. **Qualitative Faculty Feedback**: Observational notes from subject professors.
6. **Student Data Sharing Consent**: Transparent opt-in controls for parental alerts, peer tutoring, and financial counseling.

### 2. Explainable Early-Risk Diagnostic Center
Rather than an opaque black box, EduEagle calculates a composite Risk Index (0 to 100) and displays:
- **Driver Weight %**: (e.g. 32% Academic Dip, 28% Attendance Decay, 22% Financial Strain, 11% Faculty Observation, 7% Placement Gap).
- **Concrete Signal Description**: (e.g. *"Midterm exam drop from 78% to 41% in CS301"*).
- **Contextual Narrative**: Detailed root-cause background.

### 3. Multi-Stakeholder Workflow Desk with Escalation
- Roles supported: **Faculty Instructor, Academic Mentor, Head of Department (HOD), Student Counsellor, Placement Officer, Finance/Accounts Team**.
- State Machine: `Recommended` -> `Assigned` -> `In Progress` -> `Escalated` -> `Resolved`.
- **SLA Tracking and Automated Escalation**: When target hours lapse without logged contact, the system automatically escalates the case to the Head of Department.

### 4. Closed-Loop Proof of Follow-up and Outcome Verification
To mark an intervention `Resolved`, the stakeholder must submit verifiable evidence:
- Follow-up type (Remedial Clinic, Retest, Mentor Conference, Fee Installment Agreement).
- Session notes and verified artifact references (e.g. Attendance Sheet ID, Receipt ID).
- Measurable retest score (e.g. Retest Score: 76% up from 38%).
- Outcome rating: `Significantly Improved` (drops student risk index by 35 points), `Moderately Improved`, `Unchanged`, or `Needs Escalation`.

### 5. Student Portal: "My Success Hub" (Crucial Student Feature)
Students log in to access:
- **Transparent Radar**: Clear view of their academic standing, attendance velocity, and fee status.
- **My Active Support Circles**: Visibility into which faculty, mentors, and advisors are actively assigned to assist them.
- **Support Request Beacon**: 1-click self-reporting for academic tutoring, fee installment extensions, stress counseling, or placement mock drills.
- **Privacy and Consent Preferences**: Interactive toggles for parental notification permissions, peer tutoring opt-ins, and financial aid counseling.

### 6. Multi-Method Authentication System
- **Phone Number + OTP Verification**: Real-world OTP flow with simulated instant autofill.
- **Google / Gmail Authentication**: 1-click Google OAuth simulation.
- **GitHub Authentication**: 1-click GitHub OAuth simulation for student developers.
- **1-Click Stakeholder Persona Switcher**: Instant evaluation testing as Student (Aarav), Faculty (Dr. Priya), Mentor (Prof. Rajesh), HOD (Dr. Sunita), Counsellor (Dr. Anita), Placement (Mr. Vikram), or Finance (Ms. Kavita).

---

## Step-by-Step Prototype Demonstration Guide

Follow these simple steps during your evaluation:

### Step 1: Start and Open the Application
Launch the server using the provided cross-platform launcher:

- **Linux / macOS**:
  ```bash
  ./start.sh
  # or: python3 server.py
  ```
- **Windows (PowerShell)**:
  ```powershell
  .\start.ps1
  # or: python server.py
  ```

Navigate your browser to:
**`http://localhost:8000`**

On phones or tablets connected to the local Wi-Fi:
**`http://192.168.31.150:8000`**

### Step 2: Explore the 360 Dossier and Explainability
1. Click the **"Student Directory"** tab.
2. Locate student **Aarav Sharma** (STU-101, Critical Risk: 86 Index).
3. Click **"360 Dossier ->"**.
4. Observe the **Explainable Risk Indicators**:
   - Academic Dip (32% weight)
   - Attendance Decay (28% weight)
   - Financial Strain (22% weight)
   - Faculty Qualitative Signal (11% weight)
5. Review the **6 Holistic Pillars** and **Student Consent Status**.

### Step 3: Trigger an SLA Escalation
1. Click the **"Intervention Desk"** tab.
2. Look at the **Escalated** column: note **INT-2026-003** (Devansh Patel) was auto-escalated to HOD Dr. Sunita Rao due to an expired 24h critical window.
3. Test manual escalation: on any active card (e.g. Aarav Sharma), click **"Escalate"**, enter a reason, and watch it immediately escalate to the HOD with an immutable audit log.

### Step 4: Submit Follow-up Proof and Close the Loop
1. On an active card (e.g. Remedial Coaching for Data Structures), click **"Submit Proof"**.
2. Select proof type: *"Retest and Quiz Examination Record"*.
3. Enter proof notes: *"Conducted 3 remedial clinics on Graph algorithms. Retest administered."*
4. Enter Retest score: *"76% (Up from 38%)"*.
5. Select Outcome: *"Significantly Improved"*.
6. Click **"Verify Proof and Close Loop"**.
7. The card moves to **Resolved**, and Aarav's live risk index drops from **86.0 (Critical) to 51.0 (Moderate)**.

### Step 5: Test the Student Portal ("What Aarav Sees")
1. Click **"Student Portal View"** in the navigation bar.
2. See the transparent **Growth Radar** and **Active Support Circles**.
3. Click **"Request Timely Help (Beacon)"**, choose a category (e.g. *Academic Tutoring*), and transmit the beacon.
4. Toggle your **Parental Notification** or **Peer Tutoring** consent settings and see them saved instantly.

### Step 6: Test Authentication Options
1. Click the User Profile in the top-right header, or Sign Out.
2. Try logging in via:
   - **Phone + OTP**: Click "Request OTP", notice the 6-digit code auto-filled, and click "Verify and Sign In".
   - **Google / Gmail**: Click "Sign In with Google".
   - **GitHub**: Click "Sign In with GitHub".
   - **1-Click Persona Switcher**: Switch instantly between Dr. Sunita (HOD), Dr. Priya (Faculty), and Aarav (Student).

### Step 7: Inspect the Ethical AI and Audit Console
1. Click the **"Ethical AI Console"** tab.
2. Review the institutional governance protections: Anti-Punishment, Non-Diagnostic Shield, and Human-in-the-Loop Override.
3. Review the **Live System Audit Trail** documenting all logins, escalations, proof verifications, and score updates.

---

## Repository Architecture & Directory Structure

```
EduEagle/
├── server.py              # Zero-dependency Python HTTP and REST API server
├── database.py            # SQLite schema, tables, seed generator & auto .env loader
├── security.py            # HMAC token signer, PBKDF2 hashing, rate limiting & RBAC
├── validator.py           # Strict payload & parameter validation engine
├── ai_assistant.py        # EagleMentor AI copilot & NEP 2020 derivation engine
├── start.sh               # Cross-platform startup launcher for Linux / macOS
├── start.ps1              # Windows PowerShell startup launcher
├── requirements.txt       # Minimal Python dependencies
├── vercel.json            # Vercel serverless deployment routing
├── edueagle.db            # Persistent SQLite database
├── README.md              # Comprehensive documentation and demo guide
├── Architecture.md        # Comprehensive architecture & design system specification
├── scripts/               # Operational, utility, and maintenance scripts
│   ├── run_tests.py       # Unified automated test runner with rate-limit isolation
│   ├── check_git_secrets.py # Comprehensive secrets & credentials security scanner
│   └── generate_assets.py # Favicons, app icons & OpenGraph SVG/PNG asset generator
├── tests/                 # Automated test suites (100% pass across all suites)
│   ├── README.md          # Test suite documentation & coverage overview
│   ├── test_new_modules.py   # 6 Core functional modules & RBAC verification
│   ├── test_frontend_seo.py  # Frontend SEO, OpenGraph & metadata verification
│   ├── test_mobile_ux.py     # Mobile responsive breakpoints & touch UX compliance
│   ├── test_security.py      # Cryptographic token tampering & rate limit checks
│   ├── test_untrusted_user.py# 20-Point defensive security & untrusted user audit
│   └── test_ai_chatbot.py    # EagleMentor AI Copilot & NEP 2020 verification
├── sql/                   # Database schemas & cloud migration scripts
│   └── supabase_schema.sql# PostgreSQL / Supabase migration schema
├── private_storage/       # Secure storage for verified intervention evidence & files
└── static/                # Single-Page Application (SPA) frontend assets
    ├── index.html         # Main dashboard and student portal interface
    ├── 404.html           # Branded 404 error page
    ├── privacy.html       # Institutional privacy policy
    ├── terms.html         # Terms of service
    ├── thank-you.html     # Support submission confirmation
    ├── robots.txt         # Search engine crawler policies
    ├── sitemap.xml        # XML sitemap
    ├── site.webmanifest   # PWA manifest
    ├── favicon.svg        # Enterprise SVG shield favicon
    ├── css/
    │   └── style.css      # Enterprise institutional design system tokens
    ├── js/
    │   ├── app.js         # SPA controller, API client, toast engine, workflow state
    │   ├── charts.js      # Zero-dependency HTML5 Canvas radar and donut charts
    │   └── analytics.js   # Privacy-preserving event analytics logger
    └── images/
        ├── og-image.png   # OpenGraph social preview banner (1200x630)
        └── og-image.svg   # Scalable OpenGraph social banner vector
```

- **Backend**: Python 3.12+ Standard Library (`http.server`, `sqlite3`, `json`, `urllib`, `hmac`, `hashlib`).
- **Database**: SQLite 3 with ACID transactions, atomic row locks, and audit logging.
- **Frontend**: Vanilla Modern JavaScript (ES6+), responsive CSS3 custom design tokens, vector SVG iconography. Zero external CDN dependencies required; runs 100% reliably in any offline or air-gapped network environment.

---

## Verification & Automated Test Suites

EduEagle includes 6 comprehensive verification suites covering functional workflows, mobile responsiveness, SEO compliance, cryptographic security, untrusted user defenses, and AI copilot policies.

### Run All Test Suites
```bash
python3 scripts/run_tests.py
# Backward-compatible shortcut:
python3 run_tests.py
```

### Run Security Scanner
```bash
python3 scripts/check_git_secrets.py
# Backward-compatible shortcut:
python3 check_git_secrets.py
```

### Run Individual Test Suites
```bash
python3 tests/test_new_modules.py
python3 tests/test_frontend_seo.py
python3 tests/test_mobile_ux.py
python3 tests/test_security.py
python3 tests/test_untrusted_user.py
python3 tests/test_ai_chatbot.py
```

---

## Demo Stakeholder Credentials

| Persona | Name | Role | Email | Phone |
|---|---|---|---|---|
| **Student** | Aarav Sharma | B.Tech CSE (3rd Yr) | `aarav.sharma@edueagle.edu` | `+91 98765 43210` |
| **Faculty** | Dr. Priya Nair | Associate Prof, CSE | `priya.nair@edueagle.edu` | `+91 98111 22233` |
| **Mentor** | Prof. Rajesh Verma | Senior Academic Mentor | `rajesh.verma@edueagle.edu` | `+91 98222 33344` |
| **HOD** | Dr. Sunita Rao | Head of Dept, CSE | `sunita.rao@edueagle.edu` | `+91 98333 44455` |
| **Counsellor** | Dr. Anita Desai | Campus Wellbeing Director | `anita.desai@edueagle.edu` | `+91 98444 55566` |
| **Placement** | Mr. Vikram Malhotra | Head of Career Services | `vikram.malhotra@edueagle.edu` | `+91 98555 66677` |
| **Finance** | Ms. Kavita Jain | Bursar and Financial Aid | `kavita.jain@edueagle.edu` | `+91 98666 77788` |
