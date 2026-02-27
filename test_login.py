import requests
import time

url = "http://127.0.0.1:5000"

def test_login():
    session = requests.Session()
    
    # Get the login page to initialize session
    r1 = session.get(f"{url}/login")
    print(f"Login page status: {r1.status_code}")
    
    # Try logging in with the correct hardcoded credentials
    data = {
        'username': 'admin',
        'password': 'password'
    }
    r2 = session.post(f"{url}/login", data=data, allow_redirects=True)
    print(f"Login post status: {r2.status_code}")
    print(f"Current URL after login: {r2.url}")
    
    # We expect to be redirected to the dashboard
    if "dashboard" in r2.url:
        print("SUCCESS: Successfully logged in and redirected to dashboard.")
        # Test dashboard access
        r3 = session.get(f"{url}/dashboard")
        print(f"Dashboard status: {r3.status_code}")
        
        # Test logout
        r4 = session.get(f"{url}/logout", allow_redirects=True)
        print(f"Logout status: {r4.status_code}")
        print(f"Current URL after logout: {r4.url}")
        if "login" in r4.url:
             print("SUCCESS: Successfully logged out and redirected to login.")
    else:
        print("FAILED: Did not redirect to dashboard.")
        
test_login()
