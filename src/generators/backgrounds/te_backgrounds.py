#!/usr/bin/env python
#
# te_backgrounds.py
#
# Generators for backgrounds introduced with tellurium
#
# Author P G Jones - 17/04/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import te_gen
import decay_util

class Gen130Te(te_gen.TeGen):
    """ Tellurium 130 background definition."""
    def __init__(self):
        super(Gen130Te, self).__init__("130Te2v", 130, 7.0e20) #was7.9
    def _generate(self):
        spectrum = decay_util.double_beta(2.5303, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum
