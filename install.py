# installer for lastrain
# - cut/paste based on xstats 0.2

from setup import ExtensionInstaller

def loader():
    return LastRainInstaller()

class LastRainInstaller(ExtensionInstaller):
    def __init__(self):
        super(LastRainInstaller, self).__init__(
            version="0.1",
            name='lastrain',
            description='SLE for last rain information for weewx reports',
            author="Vince Skahan",
            author_email="vince@skahan.net",
            config={
                'StdReport': {
                    'lastrain': {
                        'skin': 'lastrain',
                        'HTML_ROOT': 'lastrain'}}},
            files=[('bin/user', ['bin/user/lastrain.py']),
                   ('skins/lastrain', ['skins/lastrain/skin.conf',
                                     'skins/lastrain/index.html.tmpl'])]
            )
