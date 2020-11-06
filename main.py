from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

class MainApp(App):
#'''The layout of the buttons in app'''
    def build(self):
        layout = BoxLayout(padding=10)
        birdButton = ToggleButton(text='Birds',)
 #       birdButton.bind(on_press_button=self.on_press_button)
        layout.add_widget(birdButton)

        self.oceanButton = ToggleButton(text='Ocean',
        background_normal='C:/Users/micha/Desktop/Code/Soothing Sounds/picture/oceanpic.jpg')
        self.oceanButton.bind(on_press=self.on_press_button)
        layout.add_widget(self.oceanButton)

        return layout

#'''Logic for the button press to start and stop'''
    def on_press_button(self, *args):
        # waveSound = SoundLoader.load(
        #      'C:/Users/micha/Desktop/Code/Soothing Sounds/sounds/ocean.wav'
        #     )
        
        if self.oceanButton.state == 'down':
            self.waveSound = SoundLoader.load(
             'C:/Users/micha/Desktop/Code/Soothing Sounds/sounds/ocean.wav'
            )
        
            self.waveSound.play()
            self.waveSound.loop = True
            print('On')
        else:
            self.waveSound.stop()
            print('Off')

if __name__ == '__main__':
    app = MainApp()
    app.run()

