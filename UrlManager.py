class UrlManager(object):
    def __init__(self):
        self.new_urls = []
        self.old_urls = []

    def get_urls(self, file):
        with open(file) as f:
            self.new_urls = f.read().strip().split('\n')

    def get_new_url(self):
        new_url = self.new_urls.pop(0)
        self.old_urls.append(new_url)
        return new_url

    def old_url_size(self):
        return len(self.old_urls)
