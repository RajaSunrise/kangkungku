import time
from playwright.sync_api import sync_playwright
from app.database import SessionLocal
from app import models

def cleanup_test_user():
    db = SessionLocal()
    try:
        db.query(models.User).filter(models.User.username == "testuser").delete()
        db.commit()
        print("Cleaned up 'testuser' from database.")
    except Exception as e:
        print(f"Error during cleanup: {e}")
    finally:
        db.close()

def test_register_flow():
    cleanup_test_user()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Monitor console log and alert boxes
        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
        
        # Handle the alert box automatically
        def handle_dialog(dialog):
            print(f"DIALOG: {dialog.message}")
            dialog.accept()
        page.on("dialog", handle_dialog)
        
        # 1. Navigate to Register page
        print("Navigating to http://127.0.0.1:8000/register.html...")
        page.goto("http://127.0.0.1:8000/register.html")
        page.wait_for_load_state("networkidle")
        
        # 2. Check if email field is removed
        email_field = page.locator("input#email")
        if email_field.count() == 0:
            print("SUCCESS: Email field is NOT present on the register page.")
        else:
            print("FAILURE: Email field is still present!")
            browser.close()
            return
            
        # 3. Fill in registration details
        page.fill("input#username", "testuser")
        page.fill("input#alamat", "Jl. Test No. 3")
        page.fill("input#password", "testuser123")
        
        # Save screenshot of registration form before submitting
        page.screenshot(path="static/img/register_form_screenshot.png")
        print("Saved screenshot of registration form.")
        
        # 4. Submit the registration form
        page.click("button[type='submit']")
        print("Clicked register button. Waiting for redirect...")
        
        # Wait for redirect to login.html
        page.wait_for_url("**/login.html*")
        print(f"Redirected to: {page.url}")
        
        # 5. Log in with the registered user
        page.fill("input#username", "testuser")
        page.fill("input#password", "testuser123")
        page.screenshot(path="static/img/login_form_screenshot.png")
        page.click("button[type='submit']")
        print("Clicked login button. Waiting for dashboard redirect...")
        
        # Wait for redirect to dashboard.html
        page.wait_for_url("**/dashboard.html*")
        print(f"Successfully logged in! Current URL: {page.url}")
        page.screenshot(path="static/img/dashboard_screenshot.png")
        
        browser.close()

if __name__ == "__main__":
    test_register_flow()
    # Cleanup after test
    cleanup_test_user()
