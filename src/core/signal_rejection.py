#!/usr/bin/env python
#
# signal_rejection.py
#
# Base class for applying signal rejection to raw data. General radial rejection is taken care of
# by the FiducialRejection class.
#
# Author P G Jones - 23/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import spectrum_util
import generators
import math

class SignalRejection(object):
    """ Base class for signal rejection application."""
    def __init__(self):
        """ Initialise the energy resolution and unique name."""
        self._survival_levels = {"208Tl" : 1.00,
                                 "214Bi" : 1.00,
                                 "7Be" : 1.00,
                                 "85Kr" : 1.000,
                                 "212Bi+212Po" : 1.000,
                                 "212Po+212Bi" : 1.000}

# {"238U" : 0.0003,
  #                               "234mPa" : 0.0003,
   #                              "234U" : 0.0002,
    #                             "230Th" : 0.0002,
     #                            "226Ra" : 0.0002,
      #                           "222Rn" : 0.0002,
       #                          "218Po" : 0.0002,
        #                         "214Pb" : 0.0002,
         #                        "214Bi" : 0.0002,
          #                       "214Po" : 0.0002,
                         
   
    def apply(self, raw_data):
        """ Apply the signal rejection to the raw_data."""
        result = spectrum_util.default_raw(raw_data.GetName())
        for bin_radius in range(1, raw_data.GetNbinsY() + 1):
            for bin_energy in range(1, raw_data.GetNbinsX() + 1):
                net_count = raw_data.GetBinContent(bin_energy, bin_radius)
                survival_factor = self.get_survival_factor(raw_data.GetName(),
                                                               raw_data.GetXaxis().GetBinCenter(bin_energy),
                                                               raw_data.GetYaxis().GetBinCenter(bin_radius))
#                print survival_factor
                result.SetBinContent(bin_energy, bin_radius, net_count*survival_factor)
        return result
    ################################################################################################
    def get_survival_factor(self, name, energy, radius):
        """ Return the survival factor."""
        self._name = name
        self._energy = energy
        self._radius = radius

 #       survival_level = 1.0
        if name in self._survival_levels:
            survival_level = self._survival_levels[name]
            new_energy = energy*survival_level
#            print name + str(survival_level)+"<-----------"
        else:
            survival_level = 1.0
        return survival_level


class NoRejection(SignalRejection):
    def get_survival_factor(self, name, energy, radius):
        return 1.0
