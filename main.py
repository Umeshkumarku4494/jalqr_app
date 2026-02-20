from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.clock import Clock
import cv2
import numpy as np
import jalqr_realtime_engine as engine

class JalQRApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.camera = Camera(play=True)
        self.result_label = Label(text="Analyzing...", size_hint=(1, 0.2))

        self.layout.add_widget(self.camera)
        self.layout.add_widget(self.result_label)

        Clock.schedule_interval(self.analyze_frame, 2)
        return self.layout

    def analyze_frame(self, dt):
        texture = self.camera.texture
        if texture:
            size = texture.size
            pixels = texture.pixels
            img = np.frombuffer(pixels, np.uint8)
            img = img.reshape(size[1], size[0], 4)
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.clock import Clock
import cv2
import numpy as np
import jalqr_realtime_engine as engine

class JalQRApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.camera = Camera(play=True)
        self.result_label = Label(text="Analyzing...", size_hint=(1, 0.2))

        self.layout.add_widget(self.camera)
        self.layout.add_widget(self.result_label)

        Clock.schedule_interval(self.analyze_frame, 2)
        return self.layout

    def analyze_frame(self, dt):
        texture = self.camera.texture
        if texture:
            size = texture.size
            pixels = texture.pixels
            img = np.frombuffer(pixels, np.uint8)
            img = img.reshape(size[1], size[0], 4)
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

            result = engine.process_frame(img)
            self.result_label.text = f"STATUS: {result['status']}"

if __name__ == "__main__":
    JalQRApp().run()

            result = engine.process_frame(img)
            self.result_label.text = f"STATUS: {result['status']}"

if __name__ == "__main__":
    JalQRApp().run()

