import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import logging
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class ActionProductSearch(Action):
    def name(self) -> str:
        return "action_product_search"

    def run(self, dispatcher, tracker, domain):
        # Logic to search for products
        dispatcher.utter_message(text="Here are some options for wireless headphones under $100: 1. Sony WH-CH510 - Lightweight with great sound quality. 2. JBL Tune 500BT - Comfortable fit with long battery life. 3. Anker Soundcore Life Q10 - Affordable with deep bass.")
        return []

class ActionOrderTracking(Action):
    def name(self) -> str:
        return "action_order_tracking"

    def run(self, dispatcher, tracker, domain):
        # Logic to track an order
        order_id = tracker.get_slot("order_id")
        dispatcher.utter_message(text=f"Your order {order_id} is currently in transit and is expected to arrive by January 20th.")

class ActionDefaultFallback(Action):
    def name(self) -> str:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Sorry, I didn't quite get that. Could you rephrase.")


        return []
