# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
# Import necessary libraries
from transformers import pipeline  # Make sure pipeline is imported
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHuggingFaceFallback(Action):
    def name(self) -> str:
        return "action_huggingface_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Get the latest user message
        user_input = tracker.latest_message.get('text')

        # Initialize GPT-2 from Hugging Face
        generator = pipeline('text-generation', model='gpt2')

        # Generate a response
        gpt_response = generator(user_input, max_length=50)[0]['generated_text']

        # Send response back to the user
        dispatcher.utter_message(text=gpt_response)

        return []


class ActionManageMentalHealth(Action):
    def name(self) -> Text:
        return "action_manage_mental_health"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="It's important to talk to a therapist if you're having trouble managing your mental health. A therapist can help you navigate your feelings and provide tools to manage them effectively.")
        return []

class ActionManageStress(Action):
    def name(self) -> Text:
        return "action_manage_stress"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If you're having trouble managing your stress, a therapist can help you learn healthy stress management skills and provide guidance on problem-solving to reduce stress.")
        return []

class ActionRegulateEmotions(Action):
    def name(self) -> Text:
        return "action_regulate_emotions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="A therapist can assist you in discovering techniques to regulate your emotions, whether it's managing anxiety or anger, and help you develop a plan to ensure your emotions serve you well.")
        return []

class ActionUnhealthyCopingSkills(Action):
    def name(self) -> Text:
        return "action_unhealthy_coping_skills"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Using unhealthy coping mechanisms can create more problems. A therapist can help you find healthier ways to cope with stress and address underlying issues.")
        return []

class ActionReachGoals(Action):
    def name(self) -> Text:
        return "action_reach_goals"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If you're struggling to reach your goals, a therapist can address motivational problems and help you overcome obstacles that are preventing your success.")
        return []

class ActionImproveRelationships(Action):
    def name(self) -> Text:
        return "action_improve_relationships"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="A therapist can assist you in improving your relationships by identifying issues and providing tools to form and maintain healthier connections.")
        return []

class ActionIncreaseSelfAwareness(Action):
    def name(self) -> Text:
        return "action_increase_self_awareness"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If you want to understand your behaviors and patterns, a therapist can help increase your self-awareness and assist in breaking free from unhelpful patterns.")
        return []

class ActionDealWithTransitions(Action):
    def name(self) -> Text:
        return "action_deal_with_transitions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="During major life transitions, a therapist can offer support and guidance to help you adapt and manage the emotional impact of these changes.")
        return []

class ActionParentingSupport(Action):
    def name(self) -> Text:
        return "action_parenting_support"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="For parenting support, a therapist can provide guidance on parenting strategies and help you address any concerns or challenges you may have with your child.")
        return []

class ActionProcessTrauma(Action):
    def name(self) -> Text:
        return "action_process_trauma"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If you've experienced a traumatic event, a therapist can help you process it, prevent PTSD, and find meaning or growth from the experience.")
        return []

class ActionManageProductivity(Action):
    def name(self) -> Text:
        return "action_manage_productivity"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="When your mood affects your work, a therapist can help improve your mood and productivity through various strategies and techniques.")
        return []

class ActionAddressAppetiteSleep(Action):
    def name(self) -> Text:
        return "action_address_appetite_sleep"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Changes in appetite or sleep related to your emotional state can be addressed with a therapist, who can help you understand and manage these changes.")
        return []

class ActionAddressLosingInterest(Action):
    def name(self) -> Text:
        return "action_address_losing_interest"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Losing interest in activities you used to enjoy can be a sign of something deeper. A therapist can help you uncover the reasons for this and develop a plan to regain your interest.")
        return []

class ActionImproveSocialLife(Action):
    def name(self) -> Text:
        return "action_improve_social_life"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If your social life is suffering, a therapist can help you improve your social connections and address any underlying issues affecting your social interactions.")
        return []

class ActionChangeThinkingPatterns(Action):
    def name(self) -> Text:
        return "action_change_thinking_patterns"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="A therapist can help you identify and change unhelpful thinking patterns that impact your life and mental well-being.")
        return []

class ActionIncreaseHappiness(Action):
    def name(self) -> Text:
        return "action_increase_happiness"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If you feel like you're not as happy as you could be, a therapist can help you identify what's missing and make changes to improve your overall happiness.")
        return []

class ActionCheckMentalIllnessSymptoms(Action):
    def name(self) -> Text:
        return "action_check_mental_illness_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If you suspect you have symptoms of a mental illness, talking to a therapist can help you understand your symptoms and explore treatment options.")
        return []

class ActionStoreName(Action):
    def name(self) -> Text:
        return "action_store_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the user's name from their message
        user_name = tracker.get_slot("name")
        
        # Store the name in MongoDB or just in the slot
        # (MongoDB storage will be automatic due to the tracker store)
        if user_name:
            response = f"Nice to meet you, {user_name}!"
        else:
            response = "I didn't catch your name. Could you tell me again?"

        dispatcher.utter_message(text=response)

        # Store the name in a slot
        return [SlotSet("name", user_name)]

class ActionLoginCheck(Action):
    def name(self) -> Text:
        return "action_login_check"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_name = tracker.get_slot("name")
        if user_name:
            dispatcher.utter_message(text=f"Welcome back, {user_name}! How can I assist you today?")
        else:
            dispatcher.utter_message(text="It looks like you're not logged in. Please provide your name to proceed.")
        
        return []
        
