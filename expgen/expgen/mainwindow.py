from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

from qtpyvcp import PLUGINS
from qtpyvcp.plugins import getPlugin

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        #plugs = []
        self.pluginsCb.addItem('Select Plugin')
        for plugin, obj in PLUGINS.iteritems():
            #print('{} {}'.format(plugin, obj))
            self.pluginsCb.addItem(plugin)

        self.pluginsCb.activated.connect(self.pluginChanged)
        self.statusCb.activated[str].connect(self.statusChanged)
        self.channelNameCb.activated.connect(self.channelChanged)

        ruleTypes = ['Select Type', 'Enable', 'Text', 'Style Sheet',\
            'Style Class', 'Visible', 'None']
        for item in ruleTypes:
            self.ruleTypesCb.addItem(item)
            print(item)
        self.ruleTypesCb.activated[str].connect(self.ruleTypeChanged)

    """
    # if you read this I need the variable type returned by the plugin channel
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
                    print('{} {}'.format(channelName, type(getattr(obj, channelName).getValue())))
                    #print(type(obj.)
    """
    def pluginChanged(self, index): # status needs to be divided up into groups
        pluginId = self.pluginsCb.itemText(index)
        print(pluginId)
        self.channelNameCb.clear()
        self.statusCb.clear()

        obj = getPlugin(pluginId)
        for ch_name, ch_obj in sorted(obj.channels.items()):  # a dict
            self.channelNameCb.addItem(ch_name, type(ch_obj.getValue()).__name__)
            # print('{} {}'.format(ch_name, type(ch_obj.getValue())))

    def statusChanged(self, text):
        print(text)

    def channelChanged(self, index):
        print(self.channelNameCb.itemText(index))
        print(self.channelNameCb.itemData(index))
        self.pluginTypeLb.setText(self.channelNameCb.itemData(index))

    def ruleTypeChanged(self, text): # ruleTypeLb
        items = PLUGINS.viewitems()
        for plugin, obj in items:
            if plugin == 'status':
                print(type(obj.on()))
            #print(plugin)
            #print(obj)
        print(text)
 
