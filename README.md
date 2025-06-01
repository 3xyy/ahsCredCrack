# PROOF OF CONCEPT - Automates Credential Stuffing by Reverse Brute Force

**⚠️ IMPORTANT DISCLAIMER**  
This script is provided for **educational purposes only** to act as a proof of concept and demonstrate web automation abilities. Unauthorized use against real systems is illegal and violates ethical guidelines.

## Description

This Python script demonstrates how automated credential testing could theoretically work against school portals using Selenium. It serves as:
- A web automation learning tool
- A cybersecurity awareness demonstration
- An example of why proper authentication safeguards are necessary
```mermaid
graph TD
    A[Authentication System] --> B[Implement Account Lockout]
    A --> C[Add Multi-Factor Authentication]
    A --> D[Deploy Bot Detection]
    A --> E[Rate Limit Requests]
    A --> F[Monitor Enumeration Attempts]
    
    %% Additional Security Layers
    B --> B1[3-5 Attempts Threshold]
    B --> B2[30+ Minute Lockout Period]
    B --> B3[Admin Notification]
    
    C --> C1[TOTP/OTP Options]
    C --> C2[Biometric Fallback]
    C --> C3[Hardware Token Support]
    
    D --> D1[Behavioral Analysis]
    D --> D2[CAPTCHA Challenges]
    D --> D3[Headless Browser Detection]
    
    E --> E1[IP-Based Throttling]
    E --> E2[User-Based Throttling]
    E --> E3[Geofencing Rules]
    
    F --> F1[SIEM Integration]
    F --> F2[Real-Time Alerts]
    F --> F3[Credential Stuffing Patterns]
    
    %% New Components
    A --> G[Password Policy]
    G --> G1[Minimum 12 Characters]
    G --> G2[Breached Password Checks]
    G --> G3[No Personal Info]
    
    A --> H[Session Management]
    H --> H1[Short Timeouts]
    H --> H2[Re-authentication for Sensitive Actions]
    
    A --> I[Security Headers]
    I --> I1[Content Security Policy]
    I --> I2[Strict Transport Security]
    
    %% Visual Enhancements
    classDef red fill:#ffdddd,stroke:#ff6666;
    classDef green fill:#ddffdd,stroke:#66cc66;
    classDef blue fill:#ddddff,stroke:#6666ff;
    
```
## Technical Details

**Type of Attack Demonstrated:**  
Reverse brute force credential testing (single ID with multiple last names)

**Components:**
- Selenium WebDriver for browser automation
- Basic input field interaction
- Simple timing mechanisms
- Result validation through URL changes

## Research Methodology
**This project demonstrates how vulnerable authentication systems could potentially be exploited through open-source intelligence (OSINT) and automation.**
- Located the student portal at https://5starstudents.com/americanhs
- Discovered ID enumeration was possible through the staff directory sorting function
- Accessed public staff directory at https://fremontunified.org/american/about/staff-directory/
- Compiled a list of last names from faculty members

## Ethical Warning

🚨 **This script must NOT be used for:**
- Unauthorized access attempts
- Testing systems without permission
- Harvesting personal information
- Any illegal activities

Violations may result in:
- Legal consequences (CFAA, FERPA violations)
- Academic penalties
- Criminal charges

Legal & Ethical Considerations:
Accessing or extracting personal information without explicit authorization is illegal in most jurisdictions (violating laws like FERPA, GDPR, etc.)
School systems often have strict security policies - unauthorized access may result in legal consequences or academic penalties

Intended Use:
This material is provided solely for educational purposes to demonstrate web automation concepts
It is meant for cybersecurity professionals, educators, and students learning about:
Ethical web scraping
System vulnerability awareness
Responsible disclosure practices

Prohibited Uses:
Do not use this information to access systems without written permission
Never collect, store, or distribute personal student data
Avoid using automated tools against systems that prohibit them in their ToS

Responsibility:
The author provides this information with the expectation of ethical use
Users assume full liability for any misuse
Educational institutions should use this knowledge to strengthen their security

Ethical Alternatives:

Always seek explicit permission before testing systems
Use school-approved APIs when available
Report vulnerabilities through proper channels
By studying this material, you agree to use this knowledge lawfully and ethically.




## Legal Alternatives for Learning

1. **Authorized Penetration Testing** - Only with written permission
2. **Bug Bounty Programs** - Legal vulnerability disclosure
3. **Capture The Flag (CTF)** - Ethical hacking competitions
4. **Sandbox Environments** - Practice on intentionally vulnerable systems

## Usage Requirements

To run this demo (for educational purposes only) follow the steps below to set up and run the project locally.:

### 0. Prerequisites:
[Git](https://git-scm.com/)  [Python 3.7+](https://www.python.org/downloads/)

### 1. Clone the Repository
```bash
git clone https://github.com/3xyy/ahsCredCrack.git
cd ahsCredCrack
```

### 2. (Optional) Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install selenium pyfiglet
```

### 4. Running the file:
```bash
python ahsCredCrack.py
```
