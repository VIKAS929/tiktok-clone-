from  kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from data import data as users
from uix.videocard import VideoCard
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
Builder.load_string(
 """
 #: import FadeTransition kivy.uix.screenmanager.FadeTransition 
<Home>:
    layout: layout
    MDBoxLayout:
        orientation: 'vertical'
        ScreenManager:
            id: screen_manager
            transition:FadeTransition()
            Screen:
                name:'feed'  
                MDBoxLayout:
                    md_bg_color: [0,0,0,1]
                    size_hint_y: None
                    height: root.height - dp(50)
                    SnapScroll:
                        layout: layout
                        MDBoxLayout:
                            id: layout
                            
                            orientation: 'vertical'
                            adaptive_height: True
                            
                                
            Screen:
                name: 'discover'
                MDLabel:
                    text: 'discover'
                    halign: 'center'
            Screen:
                name: 'upload'
                MDLabel:
                    text: 'upload'
                    halign: 'center'
            Screen:
                name: 'inbox'
                MDLabel:
                    text: 'inbox'
                    halign: 'center'
            Screen:
                name: 'profile'
                MDLabel:
                    text: 'profile'
                    halign: 'center'
        MDBoxLayout:
            adaptive_height: True
            NavBar:
                screen_manager: screen_manager
                layout: layout
                
    
    """
)
class Home(Screen):
    data = []
    def __init__(self, **kw):
        for profile in users:
            _data = {
                'name': profile['name'],
                'source': profile['video'],
                'caption': profile['caption'],
                'song_name': profile['song_name'],
                'profile_pic': profile['profile_pic'],
                'likes': profile['likes'],
                'comments': profile['comments'],
                'shares': profile['album_pic'],
                'album_pic': profile['album_pic'],
            }
            self.data.append(_data)
        super().__init__(**kw)
    def on_enter(self, *args):
        for data in self.data:
            video_card = VideoCard()
            video_card.data = data
            video_card.height = Window.size[1] - dp(50)
            if self.data.index(data) == 0: # if the viedo first pla it
                video_card.video_state = 'play'
            self.layout.add_widget(video_card)

        return super().on_enter(*args)