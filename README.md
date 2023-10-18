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
``` python
from imagenet_utils import wordnetid_to_leafwordnetids
print(wordnetid_to_leafwordnetids("n02120997"))
# n01496331
```