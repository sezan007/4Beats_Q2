def search(self, item):
    # Wait until the search bar is visible
    search_bar = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.SEARCH_BAR)
    )
    search_bar.send_keys(item)