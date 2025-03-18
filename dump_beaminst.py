from argparse import ArgumentParser as ap
import ROOT as RT
from gallery_utils import read_header, provide_list
import numpy as np

read_header('gallery/ValidHandle.h')
mcprodv = 'std::vector<beam::ProtoDUNEBeamEvent>'
classes = [mcprodv]
provide_list(classes)

if __name__ == '__main__':
  parser = ap()
  parser.add_argument('-f', type=str, required=True)
  parser.add_argument('--tag', type=str, default='beamevent')
  args = parser.parse_args()
  
  
  ev = RT.gallery.Event(RT.vector(RT.string)(1, args.f))
  nevents = ev.numberOfEventsInFile()
  get_prods = ev.getValidHandle[mcprodv]
  
  for i in range(nevents):
    ev.goToEntry(i)
    prods = get_prods(RT.art.InputTag(args.tag))
    prod = prods.product()[0]
    momenta_str = [
      float(f'{p:.2f}') for p in prod.GetRecoBeamMomenta()
    ]
    print(f'Trigger:{prod.GetTimingTrigger()}, TOF:{prod.GetTOF():.2f}, '
          f'High Pres. CKov:{prod.GetCKov0Status()}, '
          f'Low Pres. CKov: {prod.GetCKov1Status()}, '
          f'Possible Momenta:{momenta_str}')
  