def convert_wavepoint(wavepoint, convert2 = None, print_table = False):
  """ Convert a mid-infrared (MIR) wavepoint (int) from a FOSS spectrometer to it's corresponding pin, wavelength or wavenumber value.
      print_table can be used to instead show a conversion table of all 1,060 (FOSS) points.
  """
    pin = wavepoint+239
    if convert2 != None:
        if convert2.lower() in ['wavelength', 'wavenumber', 'pin', 'n', 'l', 'p']:
            c = convert2.lower()[4] if len(convert2.lower()) > 3 else convert2.lower()[0]
        else:
            print('convert2 must == None, "wavelength" (or "l"), "wavenumber" (or "n") or "pin" (or "p")')

    cc = 3.858 #conversion coefficient

    wavenumber = pin*cc
    wavelength = (10**7)/wavenumber

    output_ = {'i':wavepoint, 'p':pin, 'n':wavenumber, 'l':wavelength}
    #output_ = {'i':wavepoint, 'p':pin, 'n':float('%.3f' % wavenumber), 'l':float('%.3f' % wavelength)}

    if print_table == True:
        print('{:>10}{:>12}{:>21}{:>19}' .format('Wavepoint', 'FOSS Pin', 'Wavenumber (cm-1)', 'Wavelength (nm)'))
        for i in range(1060):
            i+=1
            res = convert_wavepoint(i)
            print('{:>10}{:>12}{:>21.3f}{:>19.3f}' .format(res['i'], res['p'], res['n'], res['l']))
    else:
        return output_[c] if convert2 != None else output_
