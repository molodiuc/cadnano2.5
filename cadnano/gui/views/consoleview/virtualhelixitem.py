from cadnano.cnenum import ItemType
from cadnano.gui.views.abstractitems.abstractvirtualhelixitem import AbstractVirtualHelixItem
from cadnano.gui.controllers.itemcontrollers.virtualhelixitemcontroller import VirtualHelixItemController


class ConsoleVirtualHelixItem(AbstractVirtualHelixItem):
    FILTER_NAME = "virtual_helix"

    def __init__(self, model_virtual_helix, part_item):
        AbstractVirtualHelixItem.__init__(self, model_virtual_helix, part_item)
        self._controller = VirtualHelixItemController(self, model_virtual_helix.part(), False, False)
        self._part_item = part_item
    # end def

    ### PRIVATE SUPPORT METHODS ###
    def __hash__(self):
        """ necessary as CNConsoleItem as a base class is unhashable
        but necessary due to __init__ arg differences for whatever reason
        overload
        """
        return hash((self._id_num, self._model_part))

    def __repr__(self):
        return "Console VHI %d" % self._id_num

    ### PUBLIC SUPPORT METHODS ###
    def itemType(self):
        return ItemType.VIRTUALHELIX
    # end def

    def isModelSelected(self, document):
        """Make sure the item is selected in the model

        Args:
            document (Document): reference the the model :class:`Document`
        """
        return document.isVirtualHelixSelected(self._model_part, self._id_num)
    # end def

    def log(self, message):
        self._part_item.log(message)

    ### SLOTS ###

# end class
