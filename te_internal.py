#!/usr/bin/env python
#
# te_internal.py
#
# Example script to generate, plot and limit set for a Te Loaded detector.
#
# Author P G Jones - 24/12/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author E Arushanova - 31/07/13 <e.arushanova@qmul.ac.uk. : Second revision
####################################################################################################
import os
import time
import te_data_gen
import simulation
import energy_resolution
import signal_rejection
import fiducial_rejection
import plot_data
import colour_scheme
import line_style
import limit_calculator
import limit_techniques


start_time = time.clock()
#limit_file = open("limits_212Bi.txt", "w")

te_generator = te_data_gen.TeDataGen(780000, 0.3)
raw_data = te_generator.generate()
print "Finished generation in", time.clock() - start_time, "s"
detector_sim = simulation.Simulation("Default Sim", raw_data)
detector_sim.set_pileup(True)
#detector_sim.set_pileup(False)
detector_sim.set_energy_resolution(energy_resolution.NhitResolution(200.0))
detector_sim.set_signal_rejection(signal_rejection.SignalRejection()) 
detector_sim.set_fiducial_rejection(fiducial_rejection.RadialFixedRejection(6000.0)) 
detected_data = detector_sim.generate()
print "Finsihed generation plus simulation in", time.clock() - start_time, "s"
plotter = plot_data.DetectedDataPlotter(detected_data, colour_scheme.DefaultColours(), line_style.Default())
canvas = plotter.plot(0.0, 6.0)
#canvas.Print("210BPo14C_1th_year"+".pkl","pkl")
#canvas.Print("210BiPo14C_1th_year_14C"+".pdf","pdf")
#canvas.Print("210BiPo14C_1th_year"+".C","C")


raw_input("A")
     
#limit_calc = limit_calculator.LimitCalculator(detected_data, limit_techniques.TLimit(), None)#TFeldmanCousins(3.0,3.5))
#limit_set = limit_calc.calculate([3.0])
#print limit_set

#limit_file.close()

