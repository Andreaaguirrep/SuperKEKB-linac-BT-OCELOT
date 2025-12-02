from ocelot import *
from ocelot.cpbd.elements import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.track import track_debug
import matplotlib.pyplot as plt
import time


from rfglinacbte1ROTATE import *

lat = MagneticLattice(linac)  


# --- Twiss setup ---
AX = -13.25; BX = 48.65; AY = -2.11; BY = 13.45
EMITX = 1.2e-6; EMITY = 1.2e-6
energy = 0.0328

tw0 = Twiss()
tw0.alpha_x = AX; tw0.beta_x = BX
tw0.alpha_y = AY; tw0.beta_y = BY
tw0.E = energy
tw0.emit_xn = EMITX; tw0.emit_yn = EMITY
tw0.emit_x = EMITX / energy * 0.511e-3
tw0.emit_y = EMITY / energy * 0.511e-3


tws = twiss(lat,tw0)

plot_opt_func(lat, tws,legend=False, grid=False, top_plot=['Dx','Dy'])

plt.show()