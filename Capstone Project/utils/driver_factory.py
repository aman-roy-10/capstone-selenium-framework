"""Creates WebDriver instances. webdriver-manager downloads the matching driver."""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from utils import config_reader
from utils.logger import get_logger

log = get_logger("driver")


def _chrome(headless: bool):
    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # "eager" = do not wait for slow ads/images to finish loading.
    options.page_load_strategy = "eager"
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    except Exception:
        # No internet for webdriver-manager? Fall back to Selenium's built-in manager.
        return webdriver.Chrome(options=options)


def _edge(headless: bool):
    options = EdgeOptions()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
    options.page_load_strategy = "eager"
    try:
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    except Exception:
        return webdriver.Edge(options=options)


def _firefox(headless: bool):
    options = FirefoxOptions()
    if headless:
        options.add_argument("-headless")
    options.page_load_strategy = "eager"
    try:
        from webdriver_manager.firefox import GeckoDriverManager
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    except Exception:
        return webdriver.Firefox(options=options)


def create_driver(browser=None, headless=None):
    browser = (browser or config_reader.get_browser()).lower()
    headless = config_reader.is_headless() if headless is None else headless

    builders = {"chrome": _chrome, "edge": _edge, "firefox": _firefox}
    if browser not in builders:
        raise ValueError(f"Unsupported browser '{browser}'. Use chrome, edge or firefox.")

    driver = builders[browser](headless)
    if not headless:
        driver.maximize_window()
    driver.set_page_load_timeout(config_reader.get_page_load_timeout())
    log.info("Started %s (headless=%s)", browser, headless)
    return driver
