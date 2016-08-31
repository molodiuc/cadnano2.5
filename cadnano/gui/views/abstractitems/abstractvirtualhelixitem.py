# -*- coding: utf-8 -*-
class AbstractVirtualHelixItem(object):
    """
    AbstractVirtualHelixItem is a base class for virtualhelixitem in all views.
    It includes slots that get connected in VirtualHelixItemController which
    can be overridden.

    Slots that must be overridden should raise an exception.
    """
    def __init__(self, model_virtual_helix, parent):
        self._model_vh = model_virtual_helix
        self._id_num = model_virtual_helix.idNum()
        self._part_item = parent
        self._model_part = model_virtual_helix.part()
        self.is_active = False

    def virtualHelixPropertyChangedSlot(self, virtual_helix, transform):
        pass

    def virtualHelixRemovedSlot(self):
        pass

    def strandAddedSlot(self, sender, strand):
        pass

    def setSelected(self, is_selected):
        pass
    # end def

    def getProperty(self, keys):
        return self._model_part.getVirtualHelixProperties(self._id_num, keys)
    # end def

    def getName(self):
        return self._model_part.getVirtualHelixProperties(self._id_num, 'name')
    # end def

    def getTwistPerBase(self):
        """
        Returns:
            Tuple: twist per base in degrees, eulerZ
        """
        bpr, tpr, eulerZ = self._model_part.getVirtualHelixProperties(self._id_num,
                        ['bases_per_repeat', 'turns_per_repeat', 'eulerZ'])
        return tpr*360./bpr, eulerZ

    def getAngularProperties(self):
        """
        Returns:
            Tuple: 'bases_per_repeat, 'bases_per_turn',
                    'twist_per_base', 'minor_groove_angle'
        """
        bpr, tpr, mga = self._model_part.getVirtualHelixProperties(self._id_num,
                ['bases_per_repeat', 'turns_per_repeat', 'minor_groove_angle'])
        bases_per_turn = bpr / tpr
        return bpr, bases_per_turn, tpr*360./bpr, mga

    def getModelProperties(self):
        return self._model_part.getAllVirtualHelixProperties(self._id_num)
    # end def

    def getAllPropertiesForIdNum(self, id_num):
        return self._model_part.getAllVirtualHelixProperties(id_num)
    # end def

    def setProperty(self, keys, values, id_nums=None):
        if id_nums:
            for id_num in id_nums:
                self._model_part.setVirtualHelixProperties(id_num, keys, values)
        else:
            return self._model_part.setVirtualHelixProperties(self._id_num, keys, values)
    # end def

    def setSize(self, new_size, id_nums=None):
        if id_nums:
            for id_num in id_nums:
                self._model_part.setVirtualHelixSize(id_num, new_size)
        else:
            return self._model_part.setVirtualHelixSize(self._id_num, new_size)
    # end def

    def setZ(self, new_z, id_nums=None):
        m_p = self._model_part
        if id_nums is None:
            id_nums = self._id_num

        for id_num in id_nums:
            old_z = m_p.getVirtualHelixProperties(id_num, 'z')
            if new_z != old_z:
                dz = new_z - old_z
                m_p.translateVirtualHelices([id_num], 0, 0, dz, finalize=False, use_undostack=True)
    # end def

    def getAxisPoint(self, idx):
        return self._model_part.getCoordinate(self._id_num, idx)
    # end def

    def getSize(self):
        offset, size = self._model_part.getOffsetAndSize(self._id_num)
        return size
    # end def

    def part(self):
        return self._model_part
    # end def

    def partItem(self):
        return self._part_item
    # end def

    def setActive(self, is_fwd, idx):
        """Makes active the virtual helix associated with this item."""
        self.part().setActiveVirtualHelix(self._id_num, is_fwd, idx)
    # end def

    def isActive(self):
        return self._model_part.isVirtualHelixActive(self._id_num)
    # end def

    def idNum(self):
        return self._id_num
    # end def

    def fwdStrand(self, idx):
        self._model_part.fwd_strandsets[self._id_num].getStrand(idx)
    # end def

    def revStrand(self, idx):
        self._model_part.rev_strandsets[self._id_num].getStrand(idx)
    # end def
# end class
