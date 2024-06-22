from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import math
import logging
logging.basicConfig(filename="scapper.log", level=logging.INFO)

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review", methods = ['POST', 'GET'])

def index():
    if request.method == 'POST':
        try:
            searchstring = request.form['content'].replace(" ", "")
            flifkart_url = "https://www.flipkart.com/search?q=" + searchstring 
            uclint = uReq(flifkart_url)
            #print(uclint)
            flifkart_page = uclint.read()
            flifkart_html = bs(flifkart_page, "html.parser")
            print(flifkart_html)
            bigboxes = flifkart_html.findAll("div",{"class":"cPHDOP col-12-12"})
            a = len(bigboxes)
            print(a)
            box = bigboxes[2]#one phone info
            productlink = "https://www.flipkart.com"+box.div.div.div.a['href']
            productreq = requests.get(productlink)
            print(" ")
            print(productreq)
            print(" ")
            prod_html = bs(productreq.text,"html.parser")
            print(prod_html)
            print("jai shree ram")
            comment_box = prod_html.find_all("div",{"class":"RcXBOT"})
           
                
            #for i  in comment_box:
            #   print(i.div.div.div.div.text)

            
            comment_box[0].div.div.find_all("div" ,{"class":""})[0].div.text
            for i in comment_box:
                print(i.div.div.find_all("div" ,{"class":""})[0].div.text)
                print("\n")

            filename = searchstring + ".csv"
            fw = open(filename, "w")
            headers = "product, customer Name, Rating, Heading, comment /n"
            fw.write(headers)
            reviews = []
            for commentbox in comment_box:
                try:
                    comment_box[0].div.div.find_all("div" ,{"class":""})[0].div.text

                except:
                    name = 'No Name'

                try:
                    rating = commentbox.div.div.div.p.text

                except:
                    rating = 'No rating'

                try:
                    Commenthead = commentbox.div.div.div.p.text

                except:
                    Commenthead = 'No comment  heading'

                try:
                    comtag = comment_box[0].div.div.find_all("div" ,{"class":""})

                    custcomment = comtag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: ", e)

                mydict = {"product": searchString1, "Name":name, "Rating": rating, "CommentHead": commentHead, "comment" : comment}
                reviews.append(mydict)
            logging.info("log my final result {}".format(reviews))
            return render_temoplate('result.html', reviews[0:(len(reviews)-1)])
        except Exception as e:
            print("The excetion message is: ", e)
            return 'something is wrong'
    
    else:
        return render_template('index.html')
    







