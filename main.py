from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

class MainApp(App):


    def build(self):
        layout = BoxLayout(padding=10)
        birdButton = ToggleButton(text='Birds',)
        birdButton.bind(on_press_button=self.on_press_button)
        layout.add_widget(birdButton)

        oceanButton = ToggleButton(text='Ocean',
        background_normal='C:/Users/micha/Desktop/Code/Soothing Sounds/picture/oceanpic.jpg')
        oceanButton.bind(on_press=self.on_press_button)
        layout.add_widget(oceanButton)

        return layout


    def on_press_button(self, instance):
        waveSound = SoundLoader.load(
             'C:/Users/micha/Desktop/Code/Soothing Sounds/sounds/ocean.wav'
            )
        waveSound.play()
        waveSound.loop = True
        print('You pressed the button!')

if __name__ == '__main__':
    app = MainApp()
    app.run()

