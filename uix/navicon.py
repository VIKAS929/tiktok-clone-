from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string(
"""
<Navicon>:
    adaptive_height: True
    icon: ''
    text: ''
    orientation: 'vertical'
    text_size: '14sp'
    icon_size: '35sp'
    screen: ''
    MDIcon:
        text: root.icon # I use 'text' because the icon's dont display when its set to 'icon'
        font_size: root.icon_size
        font_style: 'TikTokIcons'
        height: self.texture_size[1]
        halign: 'center'
        size_hint_y: None
    MDLabel:
        text: root.text
        font_size: root.text_size
        height: self.texture_size[1]
        halign: 'center'
        bold: True
        size_hint_y: None
        
"""
)

class NavIcon(ButtonBehavior,MDBoxLayout):
    def on_press(self):
        self.parent.parent.screen_manager.current=self.screen


