from argparse import ArgumentParser as ap
import matplotlib.pyplot as plt
import ROOT as RT
from gallery_utils import read_header, provide_list
import numpy as np
import matplotlib.pyplot as plt

read_header('gallery/ValidHandle.h')
prodv = 'std::vector<raw::OpDetWaveform>'
classes = [prodv]
provide_list(classes)



if __name__ == '__main__':
    parser = ap()
    parser.add_argument('-f', type=str, required=True)
    parser.add_argument('--event', type=int, default=0)
    parser.add_argument('--channel', type=int, default=0)
    args = parser.parse_args()
    
    
    ev = RT.gallery.Event(RT.vector(RT.string)(1, args.f))
    nevents = ev.numberOfEventsInFile()
    get_prods = ev.getValidHandle[prodv]
  
    ev.goToEntry(args.event)
    prod = get_prods(RT.art.InputTag('opdigi'))
    print(len(prod.product()))
    wfs = []
    timestamps = []
    for i in range(len(prod.product())):
        op_wf = prod.product()[i]
        
        if op_wf.ChannelNumber() == args.channel:
            wfs.append(np.array(op_wf.Waveform()))
            timestamps.append(op_wf.TimeStamp())
    full_wf = np.array(wfs).flatten()
    plt.plot(full_wf)
    plt.ylabel(f'ADC')
    plt.xlabel('Time [tick]')
    plt.title(f'Event {args.event} -- Op Channel {args.channel}')

    plt.show()
