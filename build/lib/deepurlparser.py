import tldextract

class ParseURL:
    def __init__(self, input_url):
        self.input_url = input_url
        self.extracted_data = tldextract.extract(self.input_url)

        if "https://" in input_url[:15]:
            self.scheme = "https://"
        elif "http://" in input_url[:15]:
            self.scheme = "http://"
        else:
            self.scheme = None

        self.sld = self.extracted_data[1]
        self.tld = self.extracted_data[2]
        self.subdomain = self.extracted_data[0]

        self.domain = f"{self.sld}.{self.tld}"
        self.hostname = f"{self.subdomain}{self.domain}" if not self.subdomain else f"{self.subdomain}.{self.domain}"
        self.url = f"{self.scheme}{self.subdomain}{self.sld}.{self.tld}"
        self.subdomainsld = f"{self.subdomain}{self.sld}" if not self.subdomain else f"{self.subdomain}.{self.sld}"