# upvote post
from selenium import webdriver
from time import sleep

def find_top_posts(driver):
    print("\nIn find_top function")
    posts = driver.find_elements_by_xpath('//h3[@class="_eYtD2XCVieq6emjKBH3m"]')
    post_list = []
    for i in range(5):
        print(f"{i+1 }. {posts[i].text}")
        post_list.append(posts[i])

    #Calling openpyxl function function(post_list)


def go_to_subreddit(driver, subreddit_name):
    xp = f"//span[text()='{subreddit_name}']"
    driver.find_element_by_xpath(xp).click()
    sleep(5)
    find_top_posts(driver)
    #posts = driver.find_elements_by_xpath('//h3[@class="_eYtD2XCVieq6emjKBH3m"]')
    #print(f"\nPosts in {subreddit_name} are: " )
    #post_list = []
    #for i in range(5):
    #    print(f"{i+1}. {posts[i].text}")
    #    post_list.append((posts[i]))


    sleep(5)
    driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button').click()

