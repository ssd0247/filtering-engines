"""Load the data into the primary storage medium 
(aka) working memory / RAM. The data is extracted from
the already download (if running the `load_data.py`, or
via `from load_data import *` mechanism) compressed/cloud 
folders (allowed formats : `zip`, `lzma`, `hdf5`, `bigtable`, `awsS3`).

It is brought to the working memory, in batches, size of which is
determined dynamically depending upon how much active heap memory
do we have left, and whether there is lurking ***[a type of memory fragmentation]***[memory-fragmentation]
that happens on the heap, mostly (small contrived datasets or tiny original 
datasets can reside on the stack too!).

So this module keeps track of the heap memory available to itself for downloading the
dataset into the working memory.

Assumption, runtime available working memory is just the stack
and the heap, available to the python process, in which this module is running.
No funky clsustering, complex multiprocessing-based/asyncio-based parallel 
programming constructs etc.


<!---  Hyperlinks --->
[memory-fragmentation]: https://en.wikipedia.org/wiki/Fragmentation_(computing)
"""