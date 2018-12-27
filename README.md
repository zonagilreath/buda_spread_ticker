This is a simple program which pulls the ticker object for each market tracked by Buda.com and calculates the current spread for that market.

spreadticker can be run from the command line by simply calling `$ python3 spreadticker` or the maximum number of threads for asynchronous data downloading can be supplied by including the optional `concurrency` argument with an integer like:

`$ python3 spreadticker --concurrency 10` or `$ python3 spreadticker -c 10`