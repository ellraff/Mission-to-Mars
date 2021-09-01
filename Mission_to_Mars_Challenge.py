
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Mars News
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

news_title = slide_elem.find('div', class_='content_title').get_text()
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()



# Featured images
url = 'https://spaceimages-mars.com'
browser.visit(url)

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

html = browser.html
img_soup = soup(html, 'html.parser')

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url = f'https://spaceimages-mars.com/{img_url_rel}'


# Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)


# Mars Hemispheres
url = 'https://marshemispheres.com/'
browser.visit(url)


hemisphere_image_urls = []
links = browser.find_by_css('a.product-item h3')

for i in range(len(links)-1):
    print(i)
    hemisphere = {}
    browser.find_by_css('a.product-item h3')[i].click()
    
    sample_elem = browser.find_link_by_text("Sample").first
    hemisphere['image_url'] = sample_elem['href']
    
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    hemisphere_image_urls.append(hemisphere)
    
    browser.back()



browser.quit()




