import kivy
from kivy.app import App
from kivy.uix.button import Button, ButtonBehavior
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
kivy.require('1.10.1')

class MainApp(App):
    '''The layout of the buttons in app'''
    def build(self):
        layout = BoxLayout(padding=10,orientation='vertical')
        self.rainButton = ToggleButton(text='Rain',
        background_normal='picture/rain.jpg',
        background_down='picture/rainpressed.jpg')        
        self.rainButton.bind(on_press=self.on_press_button_rain)
        layout.add_widget(self.rainButton)

        self.oceanButton = ToggleButton(text='Ocean',
        background_normal='picture/oceanpic.jpg',
        background_down='picture/oceanpicpressed.jpg')
        self.oceanButton.bind(on_press=self.on_press_button_ocean)
        layout.add_widget(self.oceanButton)

        self.birdsButton = ToggleButton(text='Birds',
        background_normal='picture/birds.jpg',
        background_down='picture/birdspressed.jpg')
        self.birdsButton.bind(on_press=self.on_press_button_bird)
        layout.add_widget(self.birdsButton)

        return layout

    '''Logic for the button press to start and stop'''
    def on_press_button_ocean(self, *args):
        if self.oceanButton.state == 'down':
            self.waveSound = SoundLoader.load(
            'sounds/ocean.wav'
            )        
            self.waveSound.play()
            self.waveSound.loop = True
            self.waveSound.volume = .5      
        else:
            self.waveSound.stop()

    def on_press_button_rain(self, *args):
        if self.rainButton.state == 'down':
            self.rainSound = SoundLoader.load(
            'sounds/rain.wav'
            )
            self.rainSound.play()
            self.rainSound.loop = True
            self.rainSound.volume = .5
        else:
            self.rainSound.stop()

    def on_press_button_bird(self, *args):
        if self.birdsButton.state == 'down':
            self.birdsSound = SoundLoader.load(
            'sounds/Relaxing-bird-sounds.wav'
            )
            self.birdsSound.play()
            self.birdsSound.loop = True
            self.birdsSound.volume = .5
        else:
            self.birdsSound.stop()


if __name__ == '__main__':
    app = MainApp()
    app.run()

