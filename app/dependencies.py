# -*- coding: utf-8 -*-	`Ç.
import os, sys, time, datetime, re
import unittest
from dateutil import parser
import re
import json
import math
from flask import Flask, Blueprint, send_from_directory, render_template, request, jsonify, redirect, session, make_response, url_for
from flask_api import status
import mercadopago
from flask_mail import Mail, Message
#from flask_session import Session
from secrets import token_urlsafe
import stripe
import google
import requests
import xml.etree.ElementTree as ElementTree
from amazon.api import AmazonAPI
from decimal import Decimal
from googletrans import Translator
import hmac, hashlib, base64, urllib
from jinja2 import contextfilter
from flask_cors import CORS, cross_origin
from threading import Thread
import operator
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
import boto3, botocore
from google.cloud import translate as google_translate
import ast
import random
import numpy as np
import operator
from bs4 import BeautifulSoup