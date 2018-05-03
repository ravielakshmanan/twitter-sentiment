import numpy as np
import matplotlib.pyplot as plt
import json
import os
import pandas as pd
from nltk.stem import SnowballStemmer
import re
restricted = ['isis']
import datetime
import codecs

# define word in and import stopwords
ls = SnowballStemmer('english')

analyze = input("Do you want to reupload the data?  If yes, write Y.  If no, write N:  ")

if analyze == 'Y':

    def word_in(word, phrase):
        return (word in phrase.split())


    stopwords_file = 'stopwords.txt'
    all_stopwords = set(codecs.open(stopwords_file, 'r', 'utf-8').read().splitlines())
    plt.ion()

    # open csv
    path_to_json = './files'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    # panda dataframe
    jsons_data = pd.DataFrame(index=None, columns=['id name', 'date', 'candidate', 'text'])

    indexcounter = 0
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            d = json.load(json_file)

        # pull date candidate and text

        for tweets in d:
            idn = tweets['id']
            date = tweets['date']
            # Put date in correct format
            newDate = re.sub('[()/]|[a-zA-Z]', '', date)
            timeSec = float(newDate) / 1000.0
            dateTime = datetime.datetime.fromtimestamp(timeSec).strftime('%Y-%m-%d %H:%M:%S.%f')
            candidate = tweets['source']['name']
            temp = tweets['text']
            temp = temp.lower()

            # remove stopwords
            for word in all_stopwords:
                if word_in(word, temp):
                    newtemp = re.sub(r'\b' + word + r'\b', '', temp)
            # remove urls
            text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', temp)
            text = text.encode('ascii', 'ignore')
            # stemming
            temp1 = text.split()
            concat = []
            for obj in temp1:
                obj = obj.decode("utf-8")
                ab = (ls.stem(obj))
                concat.append(ab)
            newtemp = " ".join(concat)
            # store in dataframe
            jsons_data.loc[indexcounter] = [idn, dateTime, candidate, newtemp]
            indexcounter = indexcounter + 1

    # Print where candidate = sen rand paul, returns a dataframe
    # df = jsons_data.query("candidate == 'Sen. Paul, Rand - (R – KY) Presidential Campaign'")

    # Print count of candidates
    # df7 = jsons_data['candidate'].value_counts()
    # print(df7)
    # jsons_data[jsons_data['candidate'] == 'Sen. Paul, Rand - (R – KY) Presidential Campaign'].head(5)

    # df1 returns all occurences of isis tweets, df2 counts by candidate
    # df1 = jsons_data[jsons_data["text"].str.contains("isis", na = False)]
    # df= df1.groupby('candidate').size()

    # Create time range
    # periodrange = pd.period_range('2-2-2016 00:00', '2-3-2016 00:00', freq='Min')

    jsons_data.to_pickle('Saved.pkl')  # save it


elif analyze == 'N':
    jsons_data = pd.read_pickle('Saved.pkl')  # load it

bucketsinput = input("How many time buckets do you want to analyze?:   ")
buckets = int(bucketsinput)

for j in range(0, buckets):
    startday = input("Please enter a start date of the form YYYY-MM-DD  ")
    endday = input("Please enter a end date of the form YYYY-MM-DD  ")

    df = jsons_data[jsons_data['candidate'] == 'Sen. Paul, Rand - (R – KY) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df3 = df2['text']

    df = jsons_data[jsons_data['candidate'] == '(Fmr.) Sen. Cruz, Ted - (R – TX) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df4 = df2['text']

    df = jsons_data[jsons_data['candidate'] == 'Sen. Rubio, Marco - (R – FL) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df5 = df2['text']

    df = jsons_data[jsons_data['candidate'] == 'Fiorina, Carly (R) Presidential Campaign ']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df6 = df2['text']

    df = jsons_data[jsons_data['candidate'] == 'Trump, Donald J. (R) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df7 = df2['text']

    df = jsons_data[jsons_data['candidate'] == '(Fmr.) Sen. Graham, Lindsey - (R – SC) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df8 = df2['text']

    df = jsons_data[jsons_data['candidate'] == 'Santorum, Rick (R) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df9 = df2['text']

    df = jsons_data[jsons_data['candidate'] == 'Bush, Jeb (R) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df10 = df2['text']

    df = jsons_data[jsons_data['candidate'] == 'Huckabee, Mike (R) Presidential Campaign ']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df11 = df2['text']

    df = jsons_data[jsons_data['candidate'] == 'Christie, Chris (R) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df12 = df2['text']

    df = jsons_data[jsons_data['candidate'] == 'Carson, Ben (R) Presidential Campaign ']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df13 = df2['text']

    df = jsons_data[jsons_data['candidate'] == '(Fmr.) Jindal, Bobby (R) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df14 = df2['text']

    df = jsons_data[jsons_data['candidate'] == '(Fmr.) Perry, Rick (R) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df15 = df2['text']

    df = jsons_data[jsons_data['candidate'] == '(Fmr.) Walker, Scott (R) Presidential Campaign\t']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df16 = df2['text']

    df = jsons_data[jsons_data['candidate'] == '(Fmr.) Gov. Kasich, John (R) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df17 = df2['text']

    df = jsons_data[jsons_data['candidate'] == '(Fmr.) Pataki, George (R) Presidential Campaign']
    df2 = df[(df['date'] > startday) & (df['date'] <= endday)]
    df18 = df2['text']

    np.savetxt(r'./files/' + startday + '_tedcruz.txt', df4.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_marcorubio.txt', df5.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_carlyfiorina.txt', df6.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_donaldtrump.txt', df7.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_lindseygraham.txt', df8.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_ricksantorum.txt', df9.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_jebbush.txt', df10.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_mikehuckabee.txt', df11.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_chrischristie.txt', df12.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_bencarson.txt', df13.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_bobbyjindal.txt', df14.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_rickperry.txt', df15.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_scottwalker.txt', df16.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_johnkasich.txt', df17.values, fmt='%s')
    np.savetxt(r'./files/' + startday + '_georgepataki.txt', df18.values, fmt='%s')