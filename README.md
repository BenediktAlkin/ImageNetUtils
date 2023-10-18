# ImageNetUtils

Utilities for working with ImageNet subsets.

# Setup
`pip install git+https://github.com/BenediktAlkin/ImageNetUtils`

# Examples
## Class index to class name
``` python
from imagenet_utils import index_to_classnames, index_to_shortest_classname
print(index_to_classnames(288))
# ['leopard', 'Panthera pardus']
print(index_to_shortest_classname(288))
# leopard
```

## Class index to WordNet id
``` python
from imagenet_utils import index_to_wordnetid
print(index_to_wordnetid(5))
# n01496331
```

## Classes of a high-level WordNet id
A good visualization of the ImageNet hierarchy can be found [here](https://observablehq.com/@mbostock/imagenet-hierarchy).

``` python
from imagenet_utils import wordnetid_to_leafwordnetids, wordnetid_to_leafnames
# n02120997 is "feline"
print(wordnetid_to_leafwordnetids("n02120997")) 
# ['n02123045', 'n02123159', 'n02123394', 'n02123597', 'n02124075', 'n02125311', 'n02127052', 'n02128385', 'n02128757', 'n02128925', 'n02129165', 'n02129604', 'n02130308']
print(wordnetid_to_leafnames("n02120997"))
# ['tabby', 'tiger cat', 'Persian cat', 'Siamese', 'Egyptian cat', 'puma', 'lynx', 'leopard', 'ounce', 'jaguar', 'lion', 'tiger', 'chetah']
```