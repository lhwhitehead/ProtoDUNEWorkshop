from argparse import ArgumentParser as ap
import ROOT as RT
from gallery_utils import read_header, provide_list
import numpy as np

read_header('gallery/ValidHandle.h')
prodv = 'std::vector<sim::SimPhotonsLite>'
classes = [prodv]
provide_list(classes)

def get_wf(photons):
  xs = [i[0] for i in photons]
  ys = [i[1] for i in photons]
  return (xs, ys)

if __name__ == '__main__':
  parser = ap()
  parser.add_argument('-f', type=str, required=True)
  parser.add_argument('-n', type=int, default=-1)
  parser.add_argument('--channel', type=int, default=0)

  args = parser.parse_args()
  
  
  ev = RT.gallery.Event(RT.vector(RT.string)(1, args.f))
  nevents = ev.numberOfEventsInFile()
  get_prods = ev.getValidHandle[prodv]
  
  for i in range(nevents):
    if args.n > 0 and i >= args.n: break
    ev.goToEntry(i)
    prod = get_prods(RT.art.InputTag('PDFastSim'))
    print(len(prod.product()))


    xs, ys = get_wf(prod.product()[args.channel].DetectedPhotons)
    