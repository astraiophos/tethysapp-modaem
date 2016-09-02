from tethys_sdk.base import TethysAppBase, url_map_maker


class Odaem(TethysAppBase):
    """
    Tethys app class for ODAEM.
    """

    name = 'ODAEM'
    index = 'modaem:home'
    icon = 'modaem/images/icon.gif'
    package = 'modaem'
    root_url = 'modaem'
    color = '#1abc9c'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='modaem',
                           controller='modaem.controllers.home'),
        )

        return url_maps