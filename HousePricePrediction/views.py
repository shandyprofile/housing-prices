import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

from django.shortcuts import render;

def home(request):
    return render(request, "home.html")

def predict(request):
    return  render(request, "predict.html")

def is_mobile(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    mobile_keywords = ['mobile', 'android', 'iphone', 'ipad']
    return any(keyword in user_agent for keyword in mobile_keywords)

def result(request):
    mobile = is_mobile(request)

    price = " ";

    if mobile:
        print("Request từ MOBILE")
        price = "MOBILE - Bedrooms: " + request.GET.get("bedrooms") + " - 150.000 USD";
    else:
        print("Request từ DESKTOP")

        bedrooms = int(request.GET.get("bedrooms"))
        if bedrooms < 3:
            price = "DESKTOP - Bedrooms: " + str(bedrooms) + " - 100.000 USD"
        elif bedrooms > 10:
            price = "DESKTOP - Bedrooms: " + str(bedrooms) + " - 400.000 USD"
        else:
            price = "DESKTOP - Bedrooms: " + str(bedrooms) + " - 200.000 USD"

    return render(request, "predict.html", {
        "result2": price
    })