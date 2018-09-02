#
# @sequence The sequence to be divided in chunks
# @chunks The number of chunks to be created
def chunkIt(sequence=seq, chunks=num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

