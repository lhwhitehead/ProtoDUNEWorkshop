from argparse import ArgumentParser as ap
import matplotlib.pyplot as plt
import ROOT as RT
from gallery_utils import read_header, provide_list
import numpy as np

read_header('gallery/ValidHandle.h')
prodv = 'std::vector<raw::RawDigit>'
classes = [prodv]
provide_list(classes)



if __name__ == '__main__':
    parser = ap()
    parser.add_argument('-f', type=str, required=True)
    parser.add_argument('-n', type=int, default=-1)
    parser.add_argument('--channel', type=int, default=0)

    args = parser.parse_args()
    
    
    ev = RT.gallery.Event(RT.vector(RT.string)(1, args.f))
    nevents = ev.numberOfEventsInFile()
    get_prods = ev.getValidHandle[prodv]
  
    ev.goToEntry(0)
    prod = get_prods(RT.art.InputTag('wirecell:daq'))
    print(len(prod.product()))

    apa1_wfs = np.zeros((2560, 6000))
    for wf in prod.product():
        channel = wf.Channel()
        if channel < 2560:
            apa1_wfs[channel] = np.array(wf.ADCs())
    

    plt.imshow(apa1_wfs.T[::-1], aspect='auto')
    plt.colorbar()
    plt.show()