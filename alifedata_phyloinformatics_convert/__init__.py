"""Top-level package for alifedata-phyloinformatics-convert."""

__author__ = """Matthew Andres Moreno"""
__email__ = 'm.more500@gmail.com'
__version__ = '0.9.0'

from .alife_dataframe_to_biopython_tree \
    import alife_dataframe_to_biopython_tree
from .alife_dataframe_to_biopython_trees \
    import alife_dataframe_to_biopython_trees
from .alife_dataframe_to_dict_of_lists import alife_dataframe_to_dict_of_lists
from .alife_dataframe_to_dendropy_tree import alife_dataframe_to_dendropy_tree
from .alife_dataframe_to_dendropy_trees \
    import alife_dataframe_to_dendropy_trees
from .alife_dataframe_to_networkx_digraph \
    import alife_dataframe_to_networkx_digraph
from .anytree_tree_to_alife_dataframe \
    import anytree_tree_to_alife_dataframe
from .biopython_tree_to_alife_dataframe \
    import biopython_tree_to_alife_dataframe
from .dendropy_tree_to_alife_dataframe import dendropy_tree_to_alife_dataframe
from .dendropy_tree_to_scipy_linkage_matrix \
    import dendropy_tree_to_scipy_linkage_matrix
from .scipy_linkage_matrix_to_dendropy_tree \
    import scipy_linkage_matrix_to_dendropy_tree

# adapted from https://stackoverflow.com/a/31079085
__all__ = [
    'alife_dataframe_to_biopython_tree',
    'alife_dataframe_to_biopython_trees',
    'alife_dataframe_to_dendropy_tree',
    'alife_dataframe_to_dendropy_trees',
    'alife_dataframe_to_network_digraph',
    'anytree_tree_to_alife_dataframe',
    'biopython_tree_to_alife_dataframe',
    'dendropy_tree_to_alife_dataframe',
    'dendropy_tree_to_scipy_linkage_matrix',
    'scipy_linkage_matrix_to_dendropy_tree',
]
