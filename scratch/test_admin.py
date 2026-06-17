import time
from playwright.sync_api import sync_playwright

def test_admin_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Monitor console log and alert boxes
        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
        page.on("dialog", lambda dialog: print(f"DIALOG: {dialog.message}") or dialog.accept())
        
        # 1. Login as admin
        print("Navigating to http://127.0.0.1:8000/login.html...")
        page.goto("http://127.0.0.1:8000/login.html")
        page.wait_for_load_state("networkidle")
        
        page.fill("input#username", "indraaja")
        page.fill("input#password", "indraaja")
        page.click("button[type='submit']")
        
        # Wait for redirect to admin.html
        page.wait_for_url("**/admin.html*")
        print(f"Logged in as admin! Redirected to: {page.url}")
        page.wait_for_load_state("networkidle")
        
        # 2. Navigate to Kelola Pengguna menu
        print("Navigating to Kelola Pengguna menu...")
        # Locate the link with id nav-users
        menu_btn = page.locator("a#nav-users").first
        menu_btn.click()
        
        # Wait for table to load
        page.wait_for_selector("tbody#users-table-body")
        page.wait_for_timeout(1000) # Wait for any fetch to complete
        
        # 3. Check if Email column header is NOT present
        email_header = page.locator("th:has-text('Email')")
        if email_header.count() == 0:
            print("SUCCESS: Email column header is NOT present in the table.")
        else:
            raise Exception("FAILURE: Email column header is still present in the table!")
            
        # 4. Click "Tambah User"
        add_btn = page.locator("button:has-text('Tambah User')").first
        add_btn.click()
        page.wait_for_selector("form[onsubmit*='createUser']")
        
        # Check if Email input field is NOT present
        email_input = page.locator("input[name='email']")
        if email_input.count() == 0:
            print("SUCCESS: Email input field is NOT present in the creation modal.")
        else:
            raise Exception("FAILURE: Email input field is still present in the creation modal!")
            
        # Fill in details
        page.fill("input[name='username']", "newadminuser")
        page.fill("input[name='alamat']", "Jl. Admin Test No. 9")
        page.fill("input[name='password']", "newadminuser123")
        page.screenshot(path="static/img/admin_add_user_modal.png")
        
        # Click Simpan
        page.click("button[type='submit']")
        print("Clicked Simpan. Waiting for table reload...")
        page.wait_for_timeout(2000)
        
        # 5. Check if user is created successfully
        user_row = page.locator("td:has-text('newadminuser')")
        if user_row.count() > 0:
            print("SUCCESS: User 'newadminuser' is listed in the user table.")
        else:
            page.screenshot(path="static/img/admin_after_add_fail.png")
            raise Exception("FAILURE: User 'newadminuser' was not created or not found in the table!")
            
        # 6. Click Edit on the user
        # Find the row containing newadminuser and click Edit within it
        row = page.locator("tr:has-text('newadminuser')").first
        edit_btn = row.locator("button:has-text('Edit')").first
        edit_btn.click()
        
        page.wait_for_selector("form[onsubmit*='updateUser']")
        print("Opened Edit User modal.")
        
        # Check if Email input field is NOT present in edit modal
        email_edit_input = page.locator("input[name='email']")
        if email_edit_input.count() == 0:
            print("SUCCESS: Email input field is NOT present in the edit modal.")
        else:
            raise Exception("FAILURE: Email input field is still present in the edit modal!")
            
        # Edit alamat
        page.fill("input[name='alamat']", "Jl. Admin Test Updated")
        page.screenshot(path="static/img/admin_edit_user_modal.png")
        page.click("button[type='submit']")
        print("Clicked Update. Waiting for table reload...")
        page.wait_for_timeout(2000)
        
        # 7. Delete the test user
        row = page.locator("tr:has-text('newadminuser')").first
        delete_btn = row.locator("button:has-text('Hapus')").first
        delete_btn.click()
        
        # Click custom modal confirm delete button
        page.wait_for_selector("button#confirm-delete-btn")
        page.click("button#confirm-delete-btn")
        print("Clicked confirm delete button. Waiting for deletion...")
        page.wait_for_timeout(2000)
        
        # Verify deletion
        user_row = page.locator("td:has-text('newadminuser')")
        if user_row.count() == 0:
            print("SUCCESS: User 'newadminuser' was successfully deleted.")
        else:
            raise Exception("FAILURE: User 'newadminuser' is still present after deletion!")
            
        browser.close()

if __name__ == "__main__":
    test_admin_flow()
