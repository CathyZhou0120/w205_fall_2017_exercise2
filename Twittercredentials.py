import tweepy

consumer_key = "aBwzAuBhDX0KShy4vaQtWlRAY";
#eg: consumer_key = "";


consumer_secret = "xNZUisl44guCKjJLC2IBnMIDsj9cbCQcrGiUrXNdtQHxbkkPmy";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "360211556-hsxBM1esTmrBjIDBTVSAr1LrAjF8tkKs5sD13lLk";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "8YhFUDGUMHFFgtjoQRFe13DbR50ZhAibGFudnzfrwaDA7";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



