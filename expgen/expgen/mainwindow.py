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

        ruleTypes = ['Select Type', 'Enable', 'Text', 'Style Sheet',\
            'Style Class', 'Visible', 'None']
        for item in ruleTypes:
            self.ruleTypesCb.addItem(item)
            print(item)
        self.ruleTypesCb.activated[str].connect(self.ruleTypeChanged)


    # if you read this I need the variable type returned by the plugin channel
    def pluginChanged(self, text): # status needs to be divided up into groups
        print(text)
        self.channelNameCb.clear()
        self.statusCb.clear()

        """
        if text == 'status':
            statusGroups = ['Select Group', 'joint', 'spindle', 'other']
            for item in statusGroups:
                self.statusCb.addItem(item)
        else: # type(channel.getValue()).__name__
        """
        for plugin, obj in PLUGINS.iteritems():
            if plugin == text:
                for channelName in sorted(obj.channels.keys()): # a dict
                    self.channelNameCb.addItem(channelName)
                    print('{} {}'.format(channelName, type(getattr(obj, channelName).getValue())))
                    #print(type(obj.)

    def statusChanged(self, text):
        print(text)

    def ruleTypeChanged(self, text): # ruleTypeLb
        items = PLUGINS.viewitems()
        for plugin, obj in items:
            if plugin == 'status':
                print(type(obj.on()))
            #print(plugin)
            #print(obj)
        print(text)
 
