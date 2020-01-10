from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

from qtpyvcp import PLUGINS

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        #plugs = []
        self.pluginsCb.addItem('Select Plugin')
        for plugin, obj in PLUGINS.iteritems():
            #print('{} {}'.format(plugin, obj))
            self.pluginsCb.addItem(plugin)

        self.pluginsCb.activated[str].connect(self.pluginChanged)
        self.statusCb.activated[str].connect(self.statusChanged)


    def pluginChanged(self, text): # status needs to be divided up into groups
        print(text)
        self.channelNameCb.clear()
        self.statusCb.clear()

        if text == 'status':
            statusGroups = ['Select Group', 'joint', 'spindle', 'other']
            for item in statusGroups:
                self.statusCb.addItem(item)
        else: # type(channel.getValue()).__name__
            for plugin, obj in PLUGINS.iteritems():
                if plugin == text:
                    for channelName in sorted(obj.channels.keys()): # a dict
                        self.channelNameCb.addItem(channelName)
                        print(type(obj.getValue()).__name__)

    def statusChanged(self, text):
        print(text)


    # add any custom methods here
    items = []
    for plugin, obj in PLUGINS.iteritems():
        for chan_name in obj.channels:
            items.append('{}:{}'.format(plugin, chan_name))
    print(len(items))
    #print(items[0].split(':')[0])
    #self.pluginsCB.clear()

 
