from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import csv
from csv import writer
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
banned = 0
clean = 0


f = open("banchecker.txt", "a")

with open("suspects.txt") as Input_text:
	Geturls = []
	for urls in Input_text:
		Geturls.append(urls)
		driver.get(urls + "?l=english")
		id = urls[-18:]
		time.sleep(1)
		try:
			driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div/div[2]/div/div[1]/div[1]/div[2]")
			bannedtwice = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div/div[3]/div/div[1]/div[1]/div[2]").text.replace(" | Info", "").replace("\n", ", ")
			if "ban" in bannedtwice:
				print("Suspect " + id.rstrip().replace("/", "") + " is BANNED")
				print(bannedtwice)
				banned = banned + 1
				f.write("Suspect " + id.rstrip().replace("/", "") + " is BANNED: " + bannedtwice + "\n")
			else:
				print("Suspect " + id.rstrip().replace("/", "") + " is clean")
				f.write("Suspect " + id.rstrip().replace("/", "") + " is clean\n")
				clean = clean + 1
		except NoSuchElementException:
		
			try:
				driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div[1]/div[2]/div/div[1]/div[1]/div[2]")
				bannedonce = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div[1]/div[2]/div/div[1]/div[1]/div[2]").text.replace(" | Info", "").replace("\n", ", ")
				if "ban" in bannedonce:
					print("Suspect " + id.rstrip().replace("/", "") + " is BANNED")
					print(bannedonce)
					banned = banned + 1
					f.write("Suspect " + id.rstrip().replace("/", "") + " is BANNED: " + bannedonce + "\n")
				else:
					print("Suspect " + id.rstrip().replace("/", "") + " is clean")
					f.write("Suspect " + id.rstrip().replace("/", "") + " is clean\n")
					clean = clean + 1
			except NoSuchElementException:
			
				try:
					driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[2]/div")
					bannedonce_pp = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[2]/div").text.replace(" | Info", "").replace("\n", ", ")
					if "ban" in bannedonce_pp:
						print("Suspect " + id.rstrip().replace("/", "") + " is BANNED")
						print(bannedonce_pp)
						banned = banned + 1
						f.write("Suspect " + id.rstrip().replace("/", "") + " is BANNED: " + bannedonce_pp + "\n")
					else:
						print("Suspect " + id.rstrip().replace("/", "") + " is clean")
						clean = clean + 1
						f.write("Suspect " + id.rstrip().replace("/", "") + " is clean\n")

				except NoSuchElementException:
					print("Suspect " + id.rstrip().replace("/", "") + " is clean")
					f.write("Suspect " + id.rstrip().replace("/", "") + " is clean\n")
					clean = clean + 1

		print("\n")
	time.sleep(2)
	
print("Total: " + str(banned) + " banned player(s), " + str(clean) + " clean player(s)")
f.close()
