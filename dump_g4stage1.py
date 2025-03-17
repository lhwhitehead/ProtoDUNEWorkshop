from argparse import ArgumentParser as ap
import ROOT as RT
from gallery_utils import read_header, provide_list
import numpy as np

read_header('gallery/ValidHandle.h')
mcpartsv = 'std::vector<simb::MCParticle>'
classes = [mcpartsv]
provide_list(classes)

if __name__ == '__main__':
  parser = ap()
  parser.add_argument('-f', type=str, required=True)
  parser.add_argument('-n', type=int, default=-1)

  args = parser.parse_args()
  
  
  ev = RT.gallery.Event(RT.vector(RT.string)(1, args.f))
  nevents = ev.numberOfEventsInFile()
  get_parts = ev.getValidHandle[mcpartsv]
  
  for i in range(nevents):
    if args.n > 0 and i >= args.n: break
    ev.goToEntry(i)
    parts_prod = get_parts(RT.art.InputTag('largeant'))
    part = parts_prod.product()[0]
    print('Event:', i, f'PDG:{part.PdgCode()}', 
          f'P:{part.P():.2f}', f'Daughters:{part.NumberDaughters()}')
    print(f'\tStart Position: {part.Position().X():.2f}, '
          f'{part.Position().Y():.2f}, {part.Position().Z():.2f}')
    print(f'\tEnd Position: {part.EndPosition().X():.2f}, '
          f'{part.EndPosition().Y():.2f}, {part.EndPosition().Z():.2f}')
    print(f'\tEnd Process: {part.EndProcess()}')