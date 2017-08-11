

# Import Lionel's tools for loading NR data
from nrutils import scsearch,gwylm

# Find simulations
# C = scsearch(nonspinning=True,verbose=True)

# # For all NR simulations of interest
# for sce in C:
#
#     # Load NR data
#     lmlist = [ (2,2), (2,1), (3,3), (3,2), (4,4), (4,3) ]
#     lmlist += [ (l,-m) for (l,m) in lmlist ]
#     y = gwylm(sce,lm=lmlist,verbose=True,clean=True)
#     g = y.ringdown(T0=10)
#
#     # Plot FD comparison of nonspinning waveform NR, lal_model, python model
#     y.plot(domain='freq')
#
#     # Plot analog TD comparison for same nr case
