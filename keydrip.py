try:
    import cloudscraper
    from bs4 import BeautifulSoup
    import yaml
    import time
except:
    print("Installing requirements...")
    import os
    os.system("pip install -r requirements.txt")
    print("Done!")
    import cloudscraper
    from bs4 import BeautifulSoup
    import yaml
    import time

class handler():
    def __init__(self, log=False) -> None:
        self.plog = log
        self.session = cloudscraper.session()
        self.name = "Keydrip"
        self.version = "1.0.0"
        self.proxies = None
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
            self.steamLoginSecure = config["steamLoginSecure"]
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        if self.login() == False:
            self.loggedIn = False
            self.log("Failed to login!", "FAILURE")
        else: 
            self.loggedIn = True
            self.log("Logged in!", "SUCCESS")
    
    def log(self, msg, type="") -> bool:
        if self.plog == False:return False
        print(f"[{type}]" if type!="" else "", f"[{self.name} v{self.version}] {msg}")
        return True

    def setCF(self) -> cloudscraper.requests.Request:return self.session.get('https://key-drop.com/')

    def clearCF(self) -> cloudscraper.requests.Request:return self.session.post('https://key-drop.com/cdn-cgi/challenge-platform/h/g/jsd/r/8423a1a43dd170d9')

    def setVioShield(self) -> cloudscraper.requests.Request:return self.session.get('https://key-drop.com/cybervio/shield/pre-check')

    def getLogin(self) -> str: self.steamURL = self.session.post('https://key-drop2.com/index.php?login').url

    def steamLogin(self) -> str:
        r = self.session.get(
            url=self.steamURL,
            cookies={"steamLoginSecure": self.steamLoginSecure},
            json={
                "openid.ns": "http://specs.openid.net/auth/2.0",
                "openid.mode": "checkid_setup",
                "openid.return_to": "https://key-drop2.com/index.php?login",
                "openid.realm": "https://key-drop2.com",
                "openid.ns.sreg": "http://openid.net/extensions/sreg/1.1",
                "openid.claimed_id": "http://specs.openid.net/auth/2.0/identifier_select",
                "openid.identity": "http://specs.openid.net/auth/2.0/identifier_select"
            },
            proxies=self.proxies
        )
        soup = BeautifulSoup(r.text, "html.parser")
        openidparams = soup.find("input", {"name": "openidparams"})["value"]
        nonce = r.cookies.get_dict()["sessionidSecureOpenIDNonce"]
        for img in soup.find_all("img"):
            if "https://avatars.cloudflare.steamstatic.com/" in img["src"]:
                self.userAvatar = img["src"]
                break
        r = self.session.post(
            url="https://steamcommunity.com/openid/login",
            cookies={"steamLoginSecure": self.steamLoginSecure},
            data={
                "action": "steam_openid_login",
                "openid.mode": "checkid_setup",
                "openidparams": openidparams,
                "nonce": nonce
            },
            proxies=self.proxies
        )
        self.keydropLoginURL = r.url
        return self.keydropLoginURL
    
    def keydropLogin(self) -> cloudscraper.requests.Request:
        self.setVioShield()
        self.clearCF()
        return self.session.get(url=self.keydropLoginURL)     

    def getBalance(self, force=False) -> bool or list:
        try:
            self.setCF()
            self.clearCF()
            self.setVioShield()
            a = self.session.get(url="https://key-drop.com/balance").json()
            if force==True: return [a["gold"], a["pkt"]]
            self.log(f"Balance: {a['gold']} gold, {a['pkt']}$", "SUCCESS")
            return [a["gold"], a["pkt"]]
        except:
            return False

    def login(self) -> bool:
        self.setCF()
        self.setVioShield()
        self.clearCF()
        self.getLogin()
        self.steamLogin()
        self.keydropLogin()
        if type(self.getBalance(force=True)[0]) != int: return False
        return True
    
    def reedemCode(self, code:str) -> bool or int:
        if self.loggedIn == False: 
            self.log("Not logged in!", "FAILURE")
            return False
        r = self.session.post(
            url="https://key-drop.com/apiData/Bonus/gold_activation_code",
            json={"promoCode": code},
            proxies=self.proxies
        ).json()
        if r["status"] == False:
            self.log(r["info"], "FAILURE")
            return False
        gold = r["goldBonus"]
        self.log(f"Reedemed {gold} gold!", "SUCCESS")
        return gold



    


