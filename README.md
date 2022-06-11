# image-to-ascii

A python script to turn images into ASCII art.

## Usage

```bash
python3 image-to-ascii.py <image_file> <max_height> <character_width_to_height_ratio>
```

**image_file:** An arbitrary image file, ideally of .jpg or .png format. This can be a normal path to the file, or the filename (including extension) if it's in the `in` directory.

**max_height:** The desired height of the ASCII art, expressed in characters.

**character_width_to_height_ratio:** The ratio of width/height of the characters that will compose the ASCII art. The font used should be a *monospace* (fixed-width) font. Usually a value of 2 is fine.

### Example

```bash
python3 image-to-ascii.py monalisa.jpg 60 2.5
```

This will output a file named `monalisa.txt` in the `out` directory containing ASCII art 60 characters tall. It was previously determined that the monospace font used to display the ASCII art on github allowed approximately two and a half times as much characters in width as it did in height, hence the ratio of 2.5

```txt
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLIIILLIILLLLLLLLLLLLLLLLLLLLL
rrrrLrLLLrrrrLLLLrrrrrrLLrLLLLLLLLLLLLLLLLLLLLLLrrrrrLLLrrLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLrrrrrrrrrL
rrrrrrrrrrrrrLLLrrrrLLrLLLLLLLLLLLrrLrrrLrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrLrrrrrrrrLLLrrrrrrrrrrrrrrrrL
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrL
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr:::rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrL
r:rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr:rrrrLLLLLLLLLrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr::rrrrrr:::rr
r::rrr:::rrrrr:rrrrrrrr::::::rr:::r:r::rrLIIIIVVVVVVRRVVVVILrr:rrrrrrrrrrrrrrrr:rrr::r::::::rr:::::r
r:::::rr::::::::::::::::::::::::::::::LIIIIILLIIIVVVVVRRRRRRRVLr:::::rrrrrr::::::::::::::::::::::::r
rrr:::::::::::::::::::::::::::::::::rIILr::::::rrLLIVVVRRRRRRQQVL::::::::::::::::::::::::::::::::::r
r::::::::::::::::::::::::::::::::::LVL:'.......''':rLIVVRRRRRRRQQI::::::::::::::::::::::::::::::::::
r::::'::::::'''''''':::::::::::'::LRI:''.......''':rrLIVVRRRRRRRRQI::r::::::::::::::::'':::::::::'::
Lr::::::rr:::'''':'''':::''::'''rIVVL:'''''''''''::::rrLIVRRRRRRQRQILLrrrrr::r:::::::::'::::::::''::
ILrrLLLrrrrr::::rrr::::''''''''rLVVVr:':'''''':::::::rrLIVRRRRRRRRQVLILLLLrrrrrr::::':'''''::rr:::rr
VIILLLLLLLrrrLLLLLLLLrrr'''''':LIVVVILLLLL:':LILrLLIIIILLIVRRRRRRRRRIIIIILLLLLLLrr:''''''':::::rr:rr
VVILLLLLLLrLLLLLILLLLrLr::rrrr:LVVRVrr::rr:':Lr:':rrr:::rIVRRRRRRRRRVIIIIILILLILLL:'''''::::::rr::rr
VILLLLLLLLLLLLLIIILIIIIIILILILLIVVRRr''''''':r:'''.''':rLVRRRRRRRRRRVIIILLLLLLILLLLr:::::::::rrrrrrr
ILIIVIIIIILIILLLILIIIIIIIIIIIVVVVVVRI:''':'.:rr:'''':rLLIVRRRRRRRRRRRIIIILLLLLLLLLrrrrrrrrrLLrrrrLLL
VIIVVVIIIIIIIIIIILLIIIIIIIIIIVVVVRRRVL:::':rIILr':::rLLIVVRRRRRRRRRRRVVVVVVIIIIIIIILIIILLLLIIIIIILIL
VVVVVVIIIIIIIIIIIIIIIIIIIIIIIIVVVVVRRIr::::rLLLLrr::rLLIVRRRRRRRRRRRRVVIIIIIIIIIIIIIIILLLLLLIIIIILLL
VVIVVIIIIIIIIIIIIIIIIIIIIIIIIIVVVVRRRRVLr'':rrrrrrrrLIIIVRRRRRRRRRRRRVIIIIIIIIIIIIIIIIIIIIIIIIIIILLL
VVVVVVVVIIIIIIIIIIIIIIIIIIIIILIVVVRRRVRRVI:''::rLLLIIVVVRRRRRRRRRRRRRVVIIIILLLIIIIIIIIIIIIIILIIIILII
VVVVVIVVVVIIIIIIIIIIIIIIIILLLLLVVVRRRRRRRRVIIIIIVVVVVVVVVVRRRRRRRRRRRRVIIIIIIIIIIIIIIIIIIIIILLIILLII
VVVVVVVVIVVIIIIIIILLLLLLLLLLLLLIVRRRRRRRRRRRVLLIIVVVVVIIIIIVRRRRRRRRRRRVIIIIIIIIIIIIIIIIIIIIIIILLLLI
VVVIVIIVIIIIIILLLLLLLLLLLLLLLLLLIVVVRRRRRRRVVL:rrrLLLLLLrLLIVRRRRRRRRRRVVIIIIIILLLLLLLLLLLLLLLLLLLLI
VVIIIIIIILLLLLLIIIIIIIIIIIIIIVVIVRRRRRRRRVVILr::::::r:::::rrIVVVVVVVRRRRRRVVVVVIIIVVLrrrLLLLrLLIILLI
IIIIIIIIIIILLLIIIIIIIIRVVVVVIVVRRRRRRVVILr::''''''''''''''::LIVVVIVVRRRRRRVVIIILLLLLLrrLLLLLLLIIILLI
IIIIIIIIVIILILIIILLIIVVVIVRVIVVRRRRRVVL:'''......''....'''::LIIVIIVVRRRRRRRRVVIIrrrrrrrrrLLLLLLLLLLI
IIIIIIIIIILLLLLLLLLIIIIIIIVVVVRRRRVVIL:'...............''':rLIIVVIRRRRRVVVVVRRVIILLLrrrrLrrrrrLLLLLL
IIIIIIIIVIILLrrrrLLLIIIIIVVRRRRRRVLLr:'................''':rIIIVVVVVIIILLIIIVRRRVVIILLLrrrrrrr:rrrLL
IIIIIIIIIIIIVIILLLLLLLLIVRRRRRRRIr:''...................'':rLIIILLrrrrLLLIIVVRRRRRRRVVIIIIIILrrrrrrr
VIIIIIIIIIILIIIILLLLrrIRRRRRRRRVIL:'..........----.......':rLLLLLLIIVVVRRRRRRRRRRRRRRRVVVVVVIILrrrrr
VVIIIIILLLLLLLLLLLLLIVRRRRRVRVVVIILLrr:::''...------...':rLLIVVVVRRRRRRRRRRRRRRRRRRRRRRVIIIIIIIIIIIL
VVVIILLLLLLLLLLLLLIRRRVRRRVVVVIIIIIIIIIILLLrrrrr:::::rrLIIIVRRRRRRVVVVVVVRRRRRRRRRRRRRRVVIIIIIIILIII
VVVRVIIILLLLLLLLLLVVVVVVVVVVVIVVIVVIVVILLLILLLIIIIIIIIIVVVRRRRRRRVVIVVVVRVVRRRRRRRRRRRRRVVIIVVIIIIII
VVVRRVIIIIIIIIIIIIVVRVRRRVRVVVVVVVVVVVIIIIIIIIIIIIIIVVVRRRRRRRRVVVVVVVVVIIIVVVVVRRRRRRRRVVVIIIIIIIII
VVVVVILLLLLLLLLIIVVVVVRRRRRRVVVVRVVVVVVVVIVVVVVIIIVVVRRRRRRRRRRRRRRVVVVIIIIVVVRRRRRRRVRRVVVVIIIVVIII
IVIILrrrrrrrrrrLIVVVRVRVRRVVVRVVVVVRRVVVVVVVVVIVVVVVRRRRRRRRRRRRRRVVVVIIVVVRRRRRRRRRRVVVVVVVIIILIIII
LIILLLLLLLLLLLLVVVVVVVVVVVRRVRRRRVVRRVVVVVVVVVVVVVVVRRRRRRRRRRRRVVVVVVVVVRRRRRRRRRRRRRVVVVVVVIIIIIII
IIVVVVIIIIIIVVVVVRVVVVVVVVRRVRRRRRVRRRVVRVVVVVVVVVVRRRRRRRRRRRRRRVVRRRRRRRRRRRRRRRRRRRRRRRVVVVVVVVIV
IIIIIIIIIVVVVVVVVVVVVVVVVVVRRRRRRRRRRRRRRVVVVVVVRRRRRRRRRRRRRRRRRVRRRRRRRRRRRRRRRRRRRRRVRRVRVVVVVIII
IIIIVIVVVVVVVVVVVVVVVVVVVVVRRRRRRRRRRRRRVVVVVVRRRRRRRRRRRRRRRRRRRRQQQQRRRRRRRRRRRRRRRRVVRRRVVVVVVIII
IIIVVVVVVVVVVRVVRRRRVVRRRRVRRRRRRRRRRRRVVVVVVRRRRRRRRRRRRRRRRRRRRRQRRRRRRRRRRRRRRRRRRRRRRRRVVVVVIIII
LIVVRRVVVVRVVVVIVVVVVVVVRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQRRRRRRRRRRRRRRRRRRRRRRRRRRRVVIIII
IVVVRVVVVRRVVVIIIIIIIIIIVVVRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQRRRRRRQRRRRRRRRRRRRRRRRRRRRRRRRRRRRVVVVI
IVVVRVVVRRVVVIIIIIIIIIIILIILrr:::rrLLIVVRRRRRRRRRRRRRRRRRQQQRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRVVV
IVVVRRRVRRVVVIIIIIIIVIIVVIr:'''''''':::rrrLIVRRRRRRRRRRRRRQRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRVVVVVI
IVVVRRVRRRRRVVVVIVVVVVIVIIL::::::::::::::::::rLLIVRRRRRQQQQQQQQQQQQQQQQQQQRRRRRRRRRRRRRRRRRRRRVVVVVV
IVRRRRRRRRRRRRRRVRRVVVVVVIVILLLLrrr:::::::::::::':rIVRRRRVVVRRRRVVVVVVVVRRRRRRRRRRRVVVRRRRRRRRVVRRVV
IVRRRRRRRRRRRRRRRRRRRRRRRRVVVIILLrrrrr::rrr::rLILr:rLLIIILLLIIIIIIIIIIVVVVVRRQQRRRRVVRRRRRRRRRRRRRVV
VVRRRRRRRRRRRRRRRRRRRRRRVILLLr::rLLLLrrrrrrLLr:rLIVIIILIIIIVVIVIIVVVVVVVVVVVRRQQQRQQRRRRRRRRRRRRRVVV
RRRRRRRRRRRRRRRRRRRRRRQILLLrrr:::rLIILLLLLrrrLILrrLIVVVVIVVVVVVVVIIVRRRVRRRRRRQQQQQQQRRRRRRRRRRRRVVV
RRRRRRRRRRRRRRRRRRRRRRRLILLLLLr::rrLIIIILIIILrLIIIILLIVVVVRRRVRRRVVRRRRRRRRRRRQQQQQQQRRRRRRRRRVRRVVV
RRRRQRRRRRRRRRRRRRRRRRVIILIILrrrLIIIVVVVVVVVVVVVVVVVVIIVRRRRRRRRRRRRRRRRRRQQQQQQQQQQQQRRRRRRRRRRRVVV
RRRRRRRRRRRRRRRRRRRRRRRRVVVILLLIVVVVVVVVVVVVVVVVRRRRRRRRRRQQQQQQQQQQQQQQQQQQQQQQQQQQQRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRVIIVRRRVRRRRRRRVVVVRRRRRRRRRRRRRRQQQQQQQQQQQQQQQQQQQQQQQQQRRRRRRRRRRRRRRR
RRRRRRRRRRQRRRRRRRRRRRRRRRRRVVRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQQQQQQQQQQQQQQQQQQQQQQRRRRRRRRRRRRVR
RRRRRRRQQQQRRRRRRRQQRRRRRRRRRRRRRRQRRRRRRRRRRQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQRRRRQQRRRRRRR
RRRRQRRQQRRRRRQQQQRRRRRRRRRQRRQRRRRRRRRRRRQQQQRQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQRRQQRRR
RQRQQQQQQQQQQQQQRRRRRRRRRRRRQQQQQRRRRRRRQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQRQQQQQRRR
RQQRRRQQQQRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQRRQQRRQQQQRQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQR
```
