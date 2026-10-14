import json
import os
import re
import datetime
import cloudscraper
from bs4 import BeautifulSoup

LOTTERY_META = {
    "govisetha": {"board": "NLB", "si": "ගොවිසෙත", "ta": "கொவிசெத", "en": "Govisetha", "keywords": ["GOVISETHA"]},
    "mahajana-sampatha": {"board": "NLB", "si": "මහජන සම්පත", "ta": "மஹஜன சம்பத", "en": "Mahajana Sampatha", "keywords": ["MAHAJANA", "SAMPATHA"]},
    "mega-power": {"board": "NLB", "si": "මෙගා පවර්", "ta": "மெகா பவர்", "en": "Mega Power", "keywords": ["MEGA", "POWER"]},
    "dhana-nidhanaya": {"board": "NLB", "si": "ධන නිධානය", "ta": "தன நிதானய", "en": "Dhana Nidhanaya", "keywords": ["DHANA", "NIDHANAYA"]},
    "handahana": {"board": "NLB", "si": "හඳහන", "ta": "ஹந்தஹன", "en": "Handahana", "keywords": ["HANDAHANA"]},
    "ada-sampatha": {"board": "NLB", "si": "අද සම්පත", "ta": "அத சம்பத", "en": "Ada Sampatha", "keywords": ["ADA SAMPATHA"]},
    "nlb-jaya": {"board": "NLB", "si": "NLB ජය", "ta": "NLB ஜய", "en": "NLB Jaya", "keywords": ["NLB JAYA", "JAYA"]},
    "suba-dawasak": {"board": "NLB", "si": "සුබ දවසක්", "ta": "சுப தவசக்", "en": "Suba Dawasak", "keywords": ["SUBA", "DAWASAK"]},
    "ayubo": {"board": "NLB", "si": "ආයුබෝ", "ta": "ஆயுபோ", "en": "Ayubo", "keywords": ["AYUBO"]},
    "ada-kotipathi": {"board": "DLB", "si": "අද කෝටිපති", "ta": "அத கோட்டிபதி", "en": "Ada Kotipathi", "keywords": ["ADA KOTIPATHI", "KOTIPATHI"]},
    "lagna-wasana": {"board": "DLB", "si": "ලග්න වාසනාව", "ta": "லக்ன வாசனா", "en": "Lagna Wasana", "keywords": ["LAGNA", "WASANA"]},
    "super-ball": {"board": "DLB", "si": "සුපර් බෝල්", "ta": "சுப்பர் போல்", "en": "Super Ball", "keywords": ["SUPER BALL"]},
    "shanida": {"board": "DLB", "si": "ශනිදා", "ta": "சனிதா", "en": "Shanida", "keywords": ["SHANIDA"]},
    "kapruka": {"board": "DLB",
