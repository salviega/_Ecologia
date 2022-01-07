from bs4 import BeautifulSoup
import datetime
from datetime import timedelta as td
import folium
import geopandas as gpd
from glob import glob
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from send2trash import send2trash
import shutil
import tarfile
import time
import warnings
from webdriver_manager.chrome import ChromeDriverManager

warnings.filterwarnings("ignore")

class landsatAPI:
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.chromium = ChromeDriverManager().install()

    def query(self, footprint, date, download_folder):

        # Preparing driver (chromium)
        # Donwload on "headless"
        options = Options()
        options.add_argument("window-size=1920x1080")
        options.add_experimental_option("prefs", {
            "download.default_directory": "/Users/santiagoviana/Downloads",
            "download.prompt_for_download": False,
        })
        options.headless = True
        driver = webdriver.Chrome(self.chromium, options=options)
        driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {
            'behavior': 'allow', 'downloadPath': download_folder}}
        command_result = driver.execute("send_command", params)

        # Running chormium
        # Running driver (chormium)
        driver.get('https://ers.cr.usgs.gov/login')
        time.sleep(3)

        # Login on USGS
        driver.find_element(
            By.XPATH, '//input[contains(@name, "username")]').send_keys(self.username)
        driver.find_element(
            By.XPATH, '//input[contains(@name, "password")]').send_keys(self.password)
        driver.find_element(
            By.XPATH, '//input[contains(@id, "loginButton")]').click()
        time.sleep(2)

        print('                  \n')
        print('     Logged in      ')
        print('    ===========   \n')

        # Redirect EarthExplorer
        driver.get('https://earthexplorer.usgs.gov/')
        time.sleep(3)

        # Search Criteria
        coords = list(footprint.exterior.coords)
        i = 0
        driver.find_element(
            By.XPATH, '//label[contains(@for, "latlonfmtdec")]').click()

        for coord in coords:
            if i < 4:
                longitude = str(coord[0])
                latitude = str(coord[1])
                driver.find_element(
                    By.XPATH, '//input[contains(@id, "coordEntryAdd")]').click()
                driver.find_element_by_xpath('/html/body/div[6]')\
                    .find_element_by_id('coordEntryDialogArea')\
                    .find_element_by_class_name('inputs')\
                    .find_element_by_id('latitude').send_keys(latitude)
                driver.find_element_by_xpath('/html/body/div[6]')\
                    .find_element_by_id('coordEntryDialogArea')\
                    .find_element_by_xpath('//*[@id="coordEntryDialogArea"]/div[5]')\
                    .find_element_by_id('longitude').send_keys(longitude)
                driver.find_element(
                    By.XPATH, '//button[text()[contains(., "Add")]]').click()
                i += 1
        driver.find_element(
            By.XPATH, '//input[contains(@name, "start_linked")]').send_keys(date[0])
        driver.find_element(
            By.XPATH, '//input[contains(@name, "end_linked")]').send_keys(date[1])
        driver.find_element(
            By.XPATH, '//input[contains(@title, "Data Sets")]').click()

        # Next page: Data Sets
        driver.find_element_by_xpath('//*[@id="cat_210"]/div').click()
        driver.find_element_by_xpath('//*[@id="cat_2337"]/div').click()
        driver.find_element(
            By.XPATH, '//input[contains(@id, "coll_5e81f14f59432a27")]').click()
        driver.find_element(
            By.XPATH, '//input[contains(@class, "button tabButton unselectable")][contains(@title, "Results")]').click()
        time.sleep(3)

        # Next page: Results
        # Select image for download
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        number_images = soup.find('th',{'class' :'ui-state-icons' }).get_text()
        images = []
        for item in number_images.split():
            try:
                images.append(int(item))
            except:
                continue
        number_pages = soup.find(class_='paginationControl unselectable')
        pages = None
        for item in number_pages:
            if item.find('of'):
                for _item in item.split():
                    try:
                        pages = int(_item)
                    except:
                        continue
        image = 0
        page = 1
        print('    ================ \n')
        print('     Result Content    ')
        print('    ================ \n')
        
        while (page <= pages):
            
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")    
            result_content = soup.find_all(class_='resultRowContent')
            j = 0
            for content in result_content:
                print(f'Image: {image + 1}')
                _len = len(result_content)
                print(f'Images: {images[-1]}')
                i = 0
                for _content in content.find_all('li'):
                    if i < 4:
                        print(_content.getText())
                        i += 1
                    else:
                        print("             \n")
                #time.sleep(3)

                # Donwload image
                
                downloads = driver.find_elements(By.XPATH, '//a[contains(@title, "Download Options")]')
                downloads[j].click()
                time.sleep(1)

                driver.find_element(By.XPATH, 
                    "//button[text()[contains(., '')]][contains(@class, 'btn btn-secondary productOptionsButton')]").click()
                
                time.sleep(3)
                
                driver.find_element_by_xpath(
                    '/html/body/div[6]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/button').click()

                wait_for_downloads(download_folder)
                downloading(download_folder)
                time.sleep(3)
            
                driver.find_element(By.XPATH, 
                    "//button[text()[contains(., 'Close')]][contains(@class, 'btn btn-secondary closeProductOptionsButton')]").click()
                time.sleep(3)
 
                driver.find_elements_by_xpath(
                    '//button[contains(@class, "ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close")]')[-1].click()

                time.sleep(1)
                j = j+1
                image = image + 1
                if (j == _len):

                    next_button = driver.find_element(By.XPATH, '//a[text()[contains(., "Next")]]')
                    #ext_button_disable = None
                    if (page<pages):
                        page = page + 1
                        next_button.click()
                        time.sleep(1)

                        #next_button_disable = driver.find_element(By.XPATH, '//a[text()[contains(., "Next")]]')
                    else:
                        print('     There are not more images    ')
                        print('    =========================== \n')
                        page = page + 1
                        time.sleep(3)          

def downloading(download_folder):

    print('     Downloading    ')
    print('    ============= \n')
    while any([filename.endswith(".crdownload") for filename in
               os.listdir(download_folder)]):
        # time.sleep(3)
        #print(".", end="")
        n = None
    print('     Downloaded file!    ')
    print('    ================== \n')


def extract_file(download_folder, landsat_folder):

    # Extract file
    files = glob(download_folder+'/*.tar')
    file = files[0]
    os.mkdir(file[:file.rfind(".") + 1])

    dir = [item for item in os.listdir(download_folder) if os.path.isdir(
        os.path.join(download_folder, item))]

    tar = tarfile.open(os.path.join(download_folder, file))
    tar.extractall(os.path.join(download_folder, dir[0]))
    tar.close()

    # Move to trash .tar
    send2trash(file)

    # Move file download to Landsat8 folder
    # name folder: date
    split_folder = dir[0].replace('_', ' ').split()
    name = split_folder[3]
    name = name[:4] + '-' + name[4:]
    name = name[:7] + '-' + name[7:]

    os.rename(os.path.join(download_folder, dir[0]), os.path.join(
        download_folder, name))

    shutil.move(os.path.join(download_folder, name), landsat_folder)

    print(f'     Landsat8 imagen: {name}, on the directory!    ')
    print('    ============================================ \n')


def Footprint(latitide, longitude, path_geojson):

    m = folium.Map([latitide, longitude], zoom_start=11)
    boundary = gpd.read_file(path_geojson)
    folium.GeoJson(boundary).add_to(m)

    footprint = None
    for i in boundary['geometry']:
        footprint = i
    return footprint


def wait_for_downloads(download_folder):

    print('     Waiting for the download to start     ')
    print('    ===================================  \n')
    while not any([filename.endswith('.crdownload') for filename in
                   os.listdir(download_folder)]):
        # time.sleep(3)
        #print(".", end="")
        n = None
    print('     Done!       ')
    print('    =======    \n')


def range_current_date(landsat_folder):

    # Range current date for download satellite image
    date_dir = os.listdir(landsat_folder)
    dates = [date_dir[-1], date_dir[-2]]
    date_list = []
    for date in dates:
        new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        date_list.append(new_date)
    date_range = date_list[0]-date_list[1]

    today = datetime.date.today()
    month = str(today.month)
    day = str(today.day)
    year = str(today.year)
    end = month+"/"+day+"/"+year

    start = None

    if date_range == td(days=7):
        start = today - td(days=9)
        print('                   \n')
        print('     9 days range    ')
        print('    ============== \n')
        month = str(start.month)
        day = str(start.day)
        year = str(start.year)
        start = month+"/"+day+"/"+year
        print(f'     Date range is: {start} to {end}           ')
        print('    ========================================= \n')
        return start, end
    else:
        start = today - td(days=7)
        print('                   \n')
        print('     7 days range    ')
        print('    ============== \n')
        month = str(start.month)
        day = str(start.day)
        year = str(start.year)
        start = month+"/"+day+"/"+year
        print(f'     Date range is: {start} to {end}           ')
        print('    ========================================  \n')
        return start, end
