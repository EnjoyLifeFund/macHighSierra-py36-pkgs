# (c) 2013, Bradley Young <young.bradley@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: cartesian
    version_added: "2.1"
    short_description: returns the cartesian product of lists
    description:
        - Takes the input lists and returns a list that represents the product of the input lists.
    options:
        _raw:
            description:
                - a set of lists
            required: True
"""

EXAMPLES = """

  - name: outputs the cartesian product of the supplied lists
    debug: msg="{{item}}"
    with_cartesian:
         - "{{list1}}"
         - "{{list2}}"
  - name: used as lookup changes [1, 2, 3], [a, b] into [1, a], [1, b], [2, a], [2, b], [3, a], [3, b]
    debug: msg="{{ [1,2,3]|lookup('cartesian', [a, b])}}"
"""

RETURN = """
  _list:
    description:
      - list of lists composed of elements of the input lists
    type: lists
"""

from itertools import product

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.utils.listify import listify_lookup_plugin_terms


class LookupModule(LookupBase):
    """
    Create the cartesian product of lists
    [1, 2, 3], [a, b] -> [1, a], [1, b], [2, a], [2, b], [3, a], [3, b]
    """

    def _lookup_variables(self, terms):
        """
        Turn this:
            terms == ["1,2,3", "a,b"]
        into this:
            terms == [[1,2,3], [a, b]]
        """
        results = []
        for x in terms:
            intermediate = listify_lookup_plugin_terms(x, templar=self._templar, loader=self._loader)
            results.append(intermediate)
        return results

    def run(self, terms, variables=None, **kwargs):

        terms = self._lookup_variables(terms)

        my_list = terms[:]
        if len(my_list) == 0:
            raise AnsibleError("with_cartesian requires at least one element in each list")

        return [self._flatten(x) for x in product(*my_list)]
