from modules.helpers import make_directories, critical_error_log, print_lg
from config.settings import run_in_background, disable_extensions, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.questions import default_resume_path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

try:
    make_directories([
        file_name,
        failed_file_name,
        logs_folder_path + "/screenshots",
        default_resume_path,
        generated_resume_path + "/temp"
    ])

    options = Options()

    # 🔑 Attach to existing Chrome session
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)

except Exception as e:
    print_lg("Failed to attach to existing Chrome. Is Chrome running with --remote-debugging-port=9222?")
    critical_error_log("In Opening Chrome", e)
    try:
        driver.quit()
    except:
        exit()