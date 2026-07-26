import json
import random
import requests
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request

#reads the env file and loads variables into the environment
load_dotenv("api.env")

#Intialize the flask
app=Flask(__name__)


# Checking if the input given by the user is a digit or a keyword
def process_input(mood):
        if isinstance(mood,int):
                try:
                        with open("data.json") as f:
                                data=json.load(f)
                        for detail in data["impact_level"].values():
                                min_val, max_val = detail["range"]
                                if min_val <= mood <= max_val:
                                        return random.choice(detail["keyword"])
                                        
                                        
                except FileNotFoundError:
                        pass
                return str(mood)
        else:
                return mood

  

# Getting the news using the api key
def get_news(mood):
        # Getting the api key
        api_key=os.getenv("NEWS_API_KEY")
        url="https://newsapi.org/v2/everything"
        # to avoid the error cause by giving multiple lines as an input
        params={"q":mood,"apiKey":api_key}

        # sending a request to the newsapi over the internet
        response=requests.get(url,params=params)
         #storing the data given from the internet in the data varialble in json format and then into native python type
        data=response.json()

        #creating a list which we return after getting the desirable output
        cleaned_articles=[]
        #checking if the request was successfull or not
        if data.get("status")=="ok":
                article_list=data.get("articles",[])
                if not article_list:
                        print("No Latest News found regarding this topic")
                        return []
                for article in article_list[:5]:
                        cleaned_articles.append({
                "title": article.get("title", "No title Available"),
                "description": article.get("description", "No description Available"),
                "source": article.get("source", {}).get("name", "Unknown Source"),
                "url": article.get("url", "#"),
                "image":article.get("urlToImage")
            })
        
        return cleaned_articles # returnig the output in the form of list to the home function


@app.route("/",methods=["GET","POST"])
def home():
        articles=[]
        words=""
        message=None
        if request.method=="POST":
                user_input=request.form.get("userInput","").strip()
               
                #if user enter the digit
                if user_input.isdigit():
                        number=int(user_input)
                        words=process_input(number)
        
        # user enter a custom word to search
                else:
                        words=user_input

                articles=get_news(words)

        return render_template("index.html",articles=articles,keyword=words)

if __name__=="__main__":
        app.run(debug=True)