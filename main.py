from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
import json
import requests

class MyDatabase(Widget):
    textValue = ObjectProperty(None)

    url = 'https://samplefirebaseapp-13d04.firebaseio.com/.json'

    def patch(self,instance):
        to_database = json.loads(self.textValue.text)
        requests.patch(url=self.url,json = to_database)

    def post(self,instance):

        to_database = json.loads(self.textValue.text)
        requests.post(url=self.url,json = to_database) 
    def put(self,instance):

        to_database = json.loads(self.textValue.text)
        requests.put(url=self.url,json = to_database) 

    def delete(self,instance):
        requests.delete(url=self.url[:-5]+ self.textValue.text + ".json") 

    auth_key='Ccnw5uXXrTLjVq4ghFSD7nlIp0Ov7MKFYrHWGriH'

    def get(self):
        request = requests.get(self.url+'?auth='+self.auth_key)
        data = request.json()
        self.textValue.text = json.dumps(data, indent=2)
        print(data)
    
class MyApp(App):
    def build(self):
        return MyDatabase()

if __name__=='__main__':
    MyApp().run()