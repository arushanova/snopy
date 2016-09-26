#!/usr/bin/env python
#
# colour_scheme.py
#
# Contains the colour scheme classes - maps colours to background names
#
# Author P G Jones - 24/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import ROOT

class ColourScheme(object):
    """ Returns the ROOT colour given a background name."""
    def get_colour(self, bgName):
        """ Default return black."""
        return ROOT.kBlack

class DefaultColours(ColourScheme):
    """ Default colour scheme"""
    def __init__(self):
        """ Set the default colour list."""
        self._colours = { "Generic" : ROOT.kBlack,
                          "130Te0v" : ROOT.kRed,
                          "130Te2v" : ROOT.kBlue,
                          "14C"     : ROOT.kPink,
                          "40K"     : ROOT.kBlue,
                          "39Ar"    : ROOT.kMagenta,
                          "85Kr"    : ROOT.kMagenta,
                          "232Th"   : ROOT.kGreen,
                          "238U"    : ROOT.kCyan,                         
                          "PEP"     : ROOT.kSpring,
                          "CNO"     : ROOT.kSpring,
                          "B8"      : ROOT.kSpring,
                          "Be7"     : ROOT.kSpring,
                          "234Th"   : ROOT.kOrange,
                          "234mPa" : ROOT.kOrange,
                          "234U" : ROOT.kYellow,
                          "230Th" : ROOT.kCyan,
                          "226Ra" : ROOT.kBlue,
                          "222Rn" : ROOT.kRed,
                          "218Po" : ROOT.kViolet,
                          "214Pb" : ROOT.kViolet,
                          "214Bi" : ROOT.kPink,
                          "214Po" : ROOT.kBlue,
                          "210Tl" : ROOT.kBlack,
                          "228Ra" : ROOT.kGreen,
                          "228Ac" : ROOT.kGreen,
                          "228Th" : ROOT.kSpring,
                          "224Ra" : ROOT.kAzure,
                          "220Rn" : ROOT.kAzure,
                          "216Po" : ROOT.kAzure,
                          "212Pb" : ROOT.kMagenta,
                          "212Bi" : ROOT.kMagenta,
                          "212Po" : ROOT.kMagenta, 
                          "208Tl" : ROOT.kCyan,         
                          "212Po" : ROOT.kMagenta,
                          "212Bi" : ROOT.kOrange,
                          "210Bi" : ROOT.kOrange,
                          "210Po" : ROOT.kCyan,
                          "210Pb" : ROOT.kBlue, 
                          "210BiAV" : ROOT.kOrange,
                          "210PoAV" : ROOT.kCyan,
                          "210PbAV" : ROOT.kBlue }
                        
        self._fill_colours = { 0 : ROOT.kGreen,
                               1 : ROOT.kBlue,
                               2 : ROOT.kGreen,
                               3 : ROOT.kWhite }
    def get_colour(self, bgName):
        """ Return the colour by bgName."""
        assert(isinstance(bgName, basestring))
        elements = bgName.split("+")
        colour = self._colours[ "Generic" ]
        if elements[0] in self._colours:
            colour = self._colours[ elements[0] ]
        colour += len(elements) - 1
        return colour
    def get_fill_colour(self, index):
        """ Return the colour by drawing order (index, 0 is first)."""
        if index in self._fill_colours:
            return self._fill_colours[ index ]
        else:
            return ROOT.kBlack
        
class SolarColours(DefaultColours):
    """ Default Solar colour scheme, chosen by Helen & Phil"""
    def __init__(self):
        """ Set the solar colour list."""
        self._colours = { "Generic" : ROOT.kBlack,
                          "B8"      : ROOT.kBlue,
                          "PEP"     : ROOT.kRed,
                          "CNO"     : ROOT.kGreen,
                          "Be7"     : ROOT.kMagenta,
                          "14C"     : ROOT.kGreen + 3,
                          "85Kr"    : ROOT.kYellow + 1,
                          "39Ar"    : ROOT.kCyan,
                          "40K"     : ROOT.kOrange + 1,
                          "232Th Chain"   : ROOT.kSpring + 2,
                          "238U Chain"    : ROOT.kPink + 2 }
