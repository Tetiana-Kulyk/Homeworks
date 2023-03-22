website = "https://djinni.co/"

# Ancestor
xpath_selector_1 = "//a[@data-analytics-param='login_homepage']/ancestor::li"

# Ancestor-or-self
xpath_selector_2 = "//a[@class='navbar-brand']/ancestor-or-self::a"

# Attribute
xpath_selector_3 = "//attribute::target"
css_selector_1 = "[target]"

xpath_selector_4 = "//a/attribute::rel"

# Child
xpath_selector_5 = "/html/body/div[1]/div[1]/div[1]/h1"
xpath_selector_6 = "//child::h1"

xpath_selector_7 = "//div[@class='container container_landing']/child::p"
css_selector_2 = "p:only-child"

# Descendant
xpath_selector_8 = "//div[@align='center']/descendant::a"

# Descendant-of-self
xpath_selector_9 = "//div[@class='jobs-push-briefly']/descendant-or-self::p"

# Following
xpath_selector_10 = "//div[@class='jobs-push-employer__icon']/following::h2"

# Following-sibling
xpath_selector_11 = "//div/following-sibling::h1"
css_selector_3 = "div~h1"

# Parent
xpath_selector_12 = "//a[@rel='nofollow']/parent::*"
css_selector_4 = "div>p[class='jobs-push-hero__sub-headline']"

# Preceding
xpath_selector_13 = "//div[@class='jobs-push-employer']/div/div/h2/preceding::h1"
css_selector_5 = "div+h1"

# Preceding-sibling
xpath_selector_14 = "//p[text()[contains(.,'можливість ')]]/preceding-sibling::h2"

# Last element
xpath_selector_15 = "//nav/div/ul/li[last()]"
css_selector_6 = "a[data-analytics-param='signup_homepage']:last-child"

xpath_selector_16 = "//ul[@class='jobs-push-logos__list']/li[1]/img[last()]"

# Last but one element
xpath_selector_17 = "//nav/div/ul/li[last()-1]"
xpath_selector_18 = "//div[@class='logorow']/a[last()-1]"

# Element by position
xpath_selector_19 = "//div/div[@class='container container_landing']/ul/li[position()<2]"
xpath_selector_20 = "//div[@class='logorow']/a[position()<2]"

# Title name
xpath_selector_21 = "//a[@rel]"
css_selector_7 = "a[rel]"

# Title name and value
xpath_selector_22 = "//a[@data-analytics-param='cta_signup_recruiter_homepage']"
css_selector_8 = "a[data-analytics-param='cta_signup_recruiter_homepage']"

xpath_selector_23 = "//img[@width='63']"
css_selector_9 = "img[width='63']"

# Index
xpath_selector_24 = "//li[3]/img"
xpath_selector_25 = "//div[2]/a[1]/span"

# Id
xpath_selector_26 = "//*[@id='target']"
css_selector_10 = "#target"

xpath_selector_27 = "//*[@id='cursor']"

# More than 3 steps
xpath_selector_28 = "//div[@class='row']/div/ul/li[2]/a[text()='Умови користування']"
xpath_selector_29 = "//div/div[@class='container container_landing']/ul/li/img[@width='113']"
xpath_selector_30 = "//div[@class='jobs-push-employer']/div/div/h2"

