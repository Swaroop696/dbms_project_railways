from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://codecademy.com')
try:
    elem = browser.find_element("gamut-1hwoqu3-Box ebnwbv90")
    print('Found <%s> element with that class name!'%(elem.tag_name))
except:
    print('Was not able to find an element with that name')
