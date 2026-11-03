FACTORS={'mm':0.001,'cm':0.01,'m':1,'km':1000}
def convert_length(value,src,dst):
    return value*FACTORS[src]/FACTORS[dst]
