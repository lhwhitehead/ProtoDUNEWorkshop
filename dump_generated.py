from argparse import ArgumentParser as ap
import ROOT as RT
from gallery_utils import read_header, provide_list
import numpy as np

read_header('gallery/ValidHandle.h')
mctruthv = 'std::vector<simb::MCTruth>'
classes = [mctruthv]
provide_list(classes)

if __name__ == '__main__':
  parser = ap()
  parser.add_argument('-f', type=str, required=True)
  args = parser.parse_args()
  
  
  ev = RT.gallery.Event(RT.vector(RT.string)(1, args.f))
  nevents = ev.numberOfEventsInFile()
  get_truths = ev.getValidHandle[mctruthv]
  
  for i in range(nevents):
    ev.goToEntry(i)
    truths = get_truths(RT.art.InputTag('generator'))
    truth = truths.product()[0]
    part = truth.GetParticle(0)
    print('Event:', i, part.PdgCode(), f'{part.P():.2f}', part.NumberDaughters())
    print(f'\tStart Position: {part.Position().X():.2f}, '
          f'{part.Position().Y():.2f}, {part.Position().Z():.2f}')
    print('\tN particles:', truth.NParticles())