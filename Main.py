'''
Michael Presman
'''
import selenium.webdriver as webdriver
import time
import os


def getChannelName():
    print("Please enter the channel that you would like to scrape video titles...")
    channelName = input()
    googleSearch = "https://www.google.ca/search?q=%s+youtube&oq=%s+youtube&aqs=chrome..69i57j0l5.2898j0j4&sourceid=chrome&ie=UTF-8#q=%s+youtube&*" %(channelName, channelName, channelName)
    print(googleSearch)
    return googleSearch

def googleYoutubePage():
    driver = webdriver.Chrome("/Users/michaelpresman/PycharmProjects/YoutubeChannelVideos/chromedriver")
    driver.get(getChannelName())
    element = driver.find_element_by_class_name("s") #this is where the link to the proper youtube page lives
    keys = element.text #this grabs the link to the youtube page + other information that will need to be cut
    driver.close()

    splitKeys = keys.split(" ") #this needs to be split, because aside from the link it grabs the page description, which we need to truncate
    linkToPage = splitKeys[0] #this is where the link lives

    for index, char in enumerate(linkToPage): #this loops over the link to find where the stuff beside the link begins (which is unecessary)
        if char == "\n":
            extraCrapStartsHere = index #it starts here, we know everything beyond here can be cut


    link = ""
    for i in range(extraCrapStartsHere): #the offical link will be everything in the linkToPage up to where we found suitable to cut
        link = link + linkToPage[i]

    videosPage = link + "/videos"
    print(videosPage)
    return videosPage

def getVideoTitles():
    driver = webdriver.Chrome("/Users/michaelpresman/PycharmProjects/YoutubeChannelVideos/chromedriver")
    driver.get(googleYoutubePage())


    try:
        while True:
           clickLoadMore(driver)
           time.sleep(7) #need to wait for everything to load... the new videos and the load more button
    except BaseException as e: #the exception is catching the end of the page, where there are no more videos to load aka an error
        print("Done Looping... Now Storing Video Titles to a Document...")
        scrapeTitles(driver)



def clickLoadMore(driver):
    clickButton = driver.find_element_by_class_name("load-more-button")
    for i in range(12):  # Getting the element to be clicked needed to be done through bruteforce
        clickButton.click()
        driver.implicitly_wait(1)  # need to wait per each click


def scrapeTitles(driver):
    os.chdir("/Users/michaelpresman/Desktop/")
    listFile = open(driver.title, "a")
    for title in driver.find_elements_by_class_name("yt-uix-tile-link"):
        strTitle = str(title.text)
        listFile.write(strTitle + '\n')
    listFile.close()

    print("Done")

def main():
    getVideoTitles()


main()