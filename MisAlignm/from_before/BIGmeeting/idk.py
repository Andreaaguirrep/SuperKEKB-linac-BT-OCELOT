from ocelot import *

from ocelot.gui.accelerator import *

from rfglinacbte1 import *

import time

from rfglinacbte1 import *

lat = MagneticLattice(lattice_list)

AX = -13.251547774936
BX = 48.65814978878985
AY = -2.1101459419331854
BY = 13.453044282597473
DP = .046

EMITX = 1.2023504614117648e-06
EMITY = 1.2023504614117648e-06
energy = 0.0328  # GeV

tw0 = Twiss()
tw0.alpha_x = AX
tw0.beta_x = BX
tw0.alpha_y = AY
tw0.beta_y = BY
tw0.E = energy
tw0.emit_xn = EMITX
tw0.emit_yn = EMITY
tw0.emit_x = EMITX / energy * 0.511e-3
tw0.emit_y = EMITY / energy * 0.511e-3

tws = twiss(lat, tw0)

plot_opt_func(lat, tws, top_plot=["E"], legend=True, font_size=10)
plt.show()