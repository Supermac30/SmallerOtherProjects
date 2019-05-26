"""
    The purpose of this code is to identify the reliablity of a news source.
"""

import re

deffake = ['70news.wordpress.com','americannews.com','beforeitsnews.com',\
           'bizstandardnews.com','Bloomberg.ma','thebostontribune.com',\
           'celebtricity.com','cnn-trending.com','conservative101.com',\
           'conservativefrontline.com','CountyNewsroom.info','dailybuzzlive.com',\
           'dcgazette.com','www.disclose.tv','DrudgeReport.com.co','empireherald.com',\
           'Empirenews.net','empiresports.co','firebrandleft.com','Globalresearch.ca',\
           'gossipmillsa.com','gummypost.com','huzlers.com','infowars.com',\
           'thelastlineofdefense.org','LibertyWritersNews.com','linkbeef.com',\
           'MediaMass.net','NahaDaily.com','NationalReport.net','NaturalNews.com',\
           'NBCNews.com.co','NeonNettle.com','NewsBreaksHere.com','NewsExaminer.com',\
           'News-Hound.com','TheNewsNerd.com','Newswatch33.com','TheNewYorkEvening.com',\
           'Now8News.com','Prntly.com','React365.com','RedFlagNews.com',\
           'TheReporterz.com','Stuppid.com','truetrumpers.com',\
           'undergroundnewsreport.com','UnitedMediaPublishing.com','usatoday.com.co',\
           'washingtonpost.com.co','worldtruth.tv','enenews.com',\
           'WorldNewsDailyReport.com','Yournewswire.com']
# taken mostly from wiki page 'https://en.wikipedia.org/wiki/List_of_fake_news_websites'

while True:
    userInput = str(input("input the URL of your news source\n"))
    for i in range (len(deffake)):
        find = re.search(r'(.*)' + deffake[i] + '(.*)', userInput)
        if find:
            print("This news source is greatly dicouraged, do not trust anything you read here.")
           

"""
    to do list: create a supervised machine learning algorithm that identifies traits of fake news
                find a way to check other news sources that came before for similar news
                update deffake automatically
"""
