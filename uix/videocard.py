from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.properties import DictProperty

Builder.load_string(
"""
<VideoCard>:
    md_bg_color: [0,0,0,1]
    size_hint_y: None
    video_state: 'stop'
    MDFloatLayout:
        Video:
            source: root.data['source']
            state: root.video_state
        MDBoxLayout:
            orientation: 'vertical'
            pos_hint: { 'x':0, 'y':0}
            size_hint_x: None
            width: root.width * 0.8 # 80% off the screen
            spacing: '5dp'
            padding: '5dp'
            MDLabel:
                text:root.data['name']
                height: self.texture_size[1]
                font_size: '14sp'
                size_hint_y: None
            MDLabel:
                text:root.data['caption']
                height: self.texture_size[1]
                font_size: '14sp'
                size_hint_y: None
            MDBoxLayout:
                size_hint_y: None
                height: self.minimum_height
                MDIcon:
                    icon: 'music_note'
                    size: self.texture_size
                    size_hint: None,1
                    font_size: '14sp'
                MDLabel:
                    text:root.data['song_name']
                    height: self.texture_size[1]
                    font_size: '14sp'
                    size_hint_y: None
            
        MDBoxLayout:
            orientation: 'vertical'
            pos_hint: { 'right':1, 'y':0}
            size_hint_x: None
            width: root.width * 0.2 # 20% off the screen
            spacing: '20dp'
            padding: '5dp'
            ProfileImg:
                img: root.data['profile_pic']
                
            NavIcon:
                icon: '\U0000E80A'
                text: root.data['likes']
            NavIcon:
                icon: '\U0000E808'
                text: root.data['comments']
            NavIcon:
                icon: '\U0000E80E'
                text: root.data['shares']
            
            
            
"""
)

class VideoCard(MDBoxLayout):
    data = DictProperty(defaultvalue={
        'name': "",
        'source': "",
        'caption': "",
        'song_name': "",
        'profile_pic': "",
        'likes': "",
        'comments': "",
        'shares': "",
        'album_pic': "",
    })