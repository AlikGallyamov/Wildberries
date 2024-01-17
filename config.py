from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    window_width: str = '1600'
    window_height: str = '950'
    base_url: str = 'https://www.wildberries.ru'
    remote: bool = True
    page_load_strategy: str = 'normal'
    selenoid_capabilities: dict = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
