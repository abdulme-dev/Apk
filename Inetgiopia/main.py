from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from jnius import autoclass
from android import mActivity

Intent = autoclass('android.content.Intent')

def start_clipboard_service():
    Service = autoclass('org.kivy.inetgiopia.ClipboardMonitorService')
    service_intent = Intent(mActivity, Service)
    mActivity.startForegroundService(service_intent)

class InetgiopiaApp(App):
    def build(self):
        start_clipboard_service()
        layout = BoxLayout()
        layout.add_widget(Label(text="Inetgiopia running...
Clipboard monitoring started."))
        return layout

if __name__ == "__main__":
    InetgiopiaApp().run()
