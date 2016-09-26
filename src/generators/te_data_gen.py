#!/usr/bin/env python
#
# TeDataGen
#
# Generates a full raw data set for Te loaded scintillator
#
# Author P G Jones - 05/06/2013 <p.g.jones@qmul.ac.uk> : First revision
# Author E Arushanova - 31/07/2013 <e.arushanova@qmul.ac.uk> : Second revision
# The bg levels from  https://www.snolab.ca/snoplus/private/DocDB/0005/000507/026/Backgrounds_target_0p3Te.txt
#507-v27
####################################################################################################
import generators
import data_set
import spectrum_util
import cosmogenic_gen

class TeDataGen(object):
    """ Generates a full raw data set for Te loaded scintillator."""
    def __init__(self, scint_mass, loading):
        """ Initialise the target fractions dict, etc..."""
        self._signal_fraction = 0.3408
        self._te_fractions = { "130Te2v" : 0.3408}

        self._scint_fractions = { "210Po" : 9.54e9,   
                                  "210Bi" : 7.94e9 }
        
        self._av_fractions = { "210PoAV" : 2.25e10,
                               "210BiAV" : 2.14e10 }

        self._solar_backgrounds = [ "B8" ]
        self._loading = loading
        self._scint_mass = scint_mass
        self._te_mass = (loading/100) * scint_mass
        self._radius = 6000.0
    def set_scint_fraction(self, isotope, fraction):
        """ Set the fraction of an isotope in the scintillator."""
        if isotope in self._scint_fractions:
            self._scint_fractions[isotope] = fraction
        else:
            raise("Isotope not part of the Te set.")
    def set_te_fraction(self, isotope, fraction):
        """ Set the fraction of an isotope in the Te."""
        if isotope in self._te_fractions:
            self._te_fractions[isotope] = fraction
        else:
            raise("Isotope not part of the Te set.")
    def set_av_fraction(self, isotope, fraction):
        """ Set the fraction of an isotope in the AV."""
        if isotope in self._av_fractions:
            self._av_fractions[isotope] = fraction
        else:
            raise("Isotope not part of the AV set.")

    def generate(self):
        """ Generate a raw data set for Te loaded scintillator."""
        gen_set = data_set.RawDataSet("Te%d" % self._loading)

        # Scintillator backgrounds
        for isotope, fraction in self._scint_fractions.iteritems():
#this is if I want to use the g/g  
#            energy_spectrum = generators.generators[isotope].generate(self._scint_mass * fraction)
            energy_spectrum = generators.generators[isotope].generate(fraction)
            # Apply an internal radial dependence
            spectrum = spectrum_util.apply_radial_spectrum(energy_spectrum, 
                                                           spectrum_util.internal(self._radius))
            gen_set.add_background(spectrum)
        # AV backgrounds
        for isotope, fraction in self._av_fractions.iteritems():
            energy_spectrum = generators.generators[isotope].generate(fraction)
            # Apply an internal radial dependence
            spectrum = spectrum_util.apply_radial_spectrum(energy_spectrum, 
                                                           spectrum_util.internal(self._radius))
            gen_set.add_background(spectrum)
        # Now Solar backgrounds
        for isotope in self._solar_backgrounds:
            energy_spectrum = generators.generators[isotope].generate(self._scint_mass)
            # Apply an internal radial dependence
            spectrum = spectrum_util.apply_radial_spectrum(energy_spectrum, 
                                                           spectrum_util.internal(self._radius))
            gen_set.add_background(spectrum)
        # Now Isotope backgrounds
        for isotope, fraction in self._te_fractions.iteritems():
            energy_spectrum = generators.generators[isotope].generate(self._te_mass * fraction)
            # Apply an internal radial dependence
            spectrum = spectrum_util.apply_radial_spectrum(energy_spectrum, 
                                                           spectrum_util.internal(self._radius))
            gen_set.add_background(spectrum)

        # Now the signal

        signal_energy_spectrum = generators.generators["130Te0v"].generate(self._te_mass * \
                                                                               self._signal_fraction)
        spectrum = spectrum_util.apply_radial_spectrum(signal_energy_spectrum, 
                                                       spectrum_util.internal(self._radius))
        gen_set.set_signal(spectrum)
        return gen_set
####################################################################################################
