from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # এই ফাংশনটি অ্যাপের মূল ইন্টারফেস রিটার্ন করে
        return Label(text='হ্যালো দুনিয়া! (Hello World)')

if __name__ == '__main__':
    MyApp().run()
