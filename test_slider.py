from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

try:
    driver = webdriver.Chrome(options=options)
    driver.get('http://localhost:8080/index.html')
    
    # Wait a bit for JS to run
    time.sleep(2)
    
    # Print the number of slides
    slides_count = driver.execute_script("return document.querySelectorAll('.hero-slide').length;")
    print(f"Number of slides: {slides_count}")
    
    # Check if btnNext has an event listener or if clicking it changes active slide
    btn_next = driver.execute_script("return document.getElementById('slider-next')")
    if btn_next:
        print("Next button found.")
    
    # Check active slide
    active_idx = driver.execute_script("""
        let slides = document.querySelectorAll('.hero-slide');
        for(let i=0; i<slides.length; i++) {
            if(slides[i].classList.contains('active')) return i;
        }
        return -1;
    """)
    print(f"Active slide before click: {active_idx}")
    
    # Click next
    driver.execute_script("document.getElementById('slider-next').click();")
    time.sleep(1)
    
    active_idx_after = driver.execute_script("""
        let slides = document.querySelectorAll('.hero-slide');
        for(let i=0; i<slides.length; i++) {
            if(slides[i].classList.contains('active')) return i;
        }
        return -1;
    """)
    print(f"Active slide after click: {active_idx_after}")
    
    logs = driver.get_log('browser')
    for log in logs:
        print("BROWSER LOG:", log)
        
    driver.quit()
except Exception as e:
    print(f"Selenium error: {e}")
