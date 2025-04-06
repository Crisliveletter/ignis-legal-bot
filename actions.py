from rasa_sdk import Action
class ActionDefault(Action):
    def name(self):
        return 'action_default'
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text='Acción por defecto ejecutada.')
        return []