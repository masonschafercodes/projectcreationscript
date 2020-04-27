import os
from os import path
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from config.conf import USERNAME, PASSWORD



class Folder(object):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
            
    def create_dir(self):
        self.path_schema = "C:/Users/mason/OneDrive/Development/'20/Personal"

        self.fname = input("What should I name the folder: ")


        try:
            if path.exists(f"{self.path_schema + '/' + self.fname}"):
                print("Directory Already Exists")
                return
            else:
                os.mkdir(f"{self.path_schema + '/' + self.fname}")
                os.chdir(f"{self.path_schema + '/' + self.fname}")
                print("Changed Directory and now adding README.md")
                Path('README.md').touch()
                print("Executing git init")
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
                self.driver.get("https://github.com/")
                time.sleep(2)
                self.login_ham = self.driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
                self.login_ham.click()
                self.username_click = self.driver.find_element_by_xpath('//*[@id="login_field"]')
                self.username_click.send_keys(self.username)
                self.pass_click = self.driver.find_element_by_xpath('//*[@id="password"]')
                self.pass_click.send_keys(self.password)
                self.login_click = self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
                self.login_click.click()
                self.repodropdown_click = self.driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary')
                self.repodropdown_click.click()
                self.create_repo = self.driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]')
                self.create_repo.click()
                self.repo_name = self.driver.find_element_by_xpath('//*[@id="repository_name"]')
                self.driver.implicitly_wait(1)
                self.repo_name.send_keys(self.fname)
                self.create_repo_submit = self.driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
                time.sleep(3)
                self.create_repo_submit.click()
                self.driver.close()
                os.system('git init')
                os.system('git add .')
                os.system('git commit -m "initial commit"')
                time.sleep(2)
                os.system(f'git remote add origin https://github.com/{self.username}/{self.fname + ".git"}')
                time.sleep(2)
                os.system("git push --set-upstream origin master")
                print("Opening VS Code with current directory.")
                os.system('code .')
        except OSError:
            print(f"Creation of directory {self.path_schema + '/' + self.fname} failed")
        else:
            print(f"Creation of directory {self.path_schema + '/' + self.fname} successful") 
        
        
        
if __name__ == "__main__":
    user_input = input("Create repo(y/n): ")
    if user_input == 'y':
        repo_create = Folder(USERNAME, PASSWORD)
        repo_create.create_dir()
    else:
        print("Exiting Now!")    