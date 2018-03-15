import tstarbot as ts

BASE_UNITS = set([86])
VESPENE_BUILDING_UNITS = set([88])

MINIERAL_UNITS = set([146, 147, 341, 483, 665, 666, 796, 797, 884, 885, 886, 887])
VESPENE_UNITS = set([342, 343, 344])

class ZergResourcePool(object):
  def __init__(self):
    self._bases = {}
    self._minierals = {}
    self._vespenes = {}
    self._vbs = {}

  def update(self, units):
    self._update(units)

  def _update(self, units):
    tmp_base = []
    tmp_minierals = []
    tmp_vespene = []
    tmp_vb = []
    for u in units: 
      if self._check_base(u):
        tmp_base.append(u)
      elif self._check_minieral(u):
        tmp_minierals.append(u)
      elif self._check_vespene(u):
        tmp_vespene.append(u)
      elif self._check_vespene_buildings(u):
        tmp_vb.append(u)
      else:
        # do nothing

    self._update_base(tmp_base)
    self._update_minierals(tmp_minierals)
    self._update_vespenes(tmp_vespene)
    self._update_vb(tmp_vb)

  def _update_base(self, bases):
    bids = set([])
    for base in bases:
      self._bases[base.tag] = base
      bids.add(base.tag)

    bids_curr = set(self._bases.keys())
    del_bases = bids_curr.difference(bids)
    for bid in del_bases:
      self._bases.pop(bid)

  def _update_minierals(self, minierals):
    mids = set([])
    for m in minierals:
      self._minierals[m.tag] = m
      mids.append(m.tag)

    mids_curr = set(self._minierals.keys())
    del_mids = mids_curr.difference(mids)
    for mid in del_mids:
      self._minierals.pop(mid)

  def _update_vespenes(self, vespenes):
    vids = set([])
    for v in vespenes:
      self._vespenes[v.tag] = v
      vids.append(v.tag)

    vids_curr = set(self._vespenes.keys())
    del_vids = vids_curr.difference(vids)
    for vid in del_vids:
      self._vespenes.pop(vid)

  def _update_vb(self, vbs):
    vbids = set([])
    for vb in vbs:
      self._vbs[vb.tag] = vb
      vbids.append(vb.tag)

    vbids_curr = set(self._vbs.keys())
    del_vbids = vbids_curr.difference(vbids)
    for vbid in del_vbids:
      self._vbs.pop(vbid)

  def _check_base(self, u):
    if u.unit_type in BASE_LIST and \
      u.int_attr.alliance == ALLIANCE_SELF:
      return True
    else:
      return False

  def _check_minieral(self, u):
    if u.unit_type in MINIERAL_UNITS:
      return True
    else:
      return False

  def _check_vespene(self, u):
    if u.unit_type in VESPENE_UNITS:
      return True
    else:
      return False

  def _check_vespene_buildings(self, u):
    if u.unit_type in VESPENE_BUILDING_UNITS and \
      u.int_attr.alliance == ALLIANCE_SELF:
      return True
    else:
      return False


