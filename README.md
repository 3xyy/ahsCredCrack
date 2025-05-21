# Automates Credential Stuffing by Reverse Brute Force

**⚠️ IMPORTANT DISCLAIMER**  
This script is provided for **educational purposes only** to demonstrate web automation concepts. Unauthorized use against real systems is illegal and violates ethical guidelines.

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

## Legal Alternatives for Learning

1. **Authorized Penetration Testing** - Only with written permission
2. **Bug Bounty Programs** - Legal vulnerability disclosure
3. **Capture The Flag (CTF)** - Ethical hacking competitions
4. **Sandbox Environments** - Practice on intentionally vulnerable systems

## Usage Requirements

To run this demo (for educational purposes only):

1. Install dependencies:
```bash
pip install selenium pyfiglet
