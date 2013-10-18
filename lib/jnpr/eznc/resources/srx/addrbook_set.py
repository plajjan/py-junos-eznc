# debuggin
import pdb
from lxml import etree

# 3rd-party modules
from lxml.builder import E 

# module packages
from ... import jxml as JXML
from .. import Resource

class ZoneAddrBookSet( Resource ):
  """
  [edit security zone security-zone <zone> address-book address-set <name>]

  ~! WARNING !~
  This resource is managed only as a child of the :ZoneAddrBook:
  resource.  Do not create a manager instance of this class directly

  Notes
  -------------------------------------------------------------------
    :self._name: is the address-set name

    :self.P: is the parent ZoneAddrBook object, 
    whose _name is the security zone 
  """
  PROPERTIES = [
    'description',
  ]

  def _xml_at_top(self):
    return E.security(E.zones(
      E('security-zone', E.name(self.P._name)),
      E('address-book', E('address-set', self._name))
    ))

  ### -------------------------------------------------------------------------
  ### XML reading
  ### -------------------------------------------------------------------------

  def _xml_at_res(self, xml):
    return xml.find('.//address-book/address')

  def _xml_to_py(self, as_xml, to_py ):
    Resource._r_has_xml_status( as_xml, to_py )
    Resource.copyifexists( as_xml, 'description', to_py )

  ##### -----------------------------------------------------------------------
  ##### Manager List, Catalog
  ##### -----------------------------------------------------------------------

  def _r_list(self):
    """
    """
    raise RuntimeError("Need to implement!")

  def _r_catalog(self):
    """
    """
    raise RuntimeError("Need to implement!")