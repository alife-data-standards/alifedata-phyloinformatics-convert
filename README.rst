==================================
alifedata-phyloinformatics-convert
==================================


.. image:: https://img.shields.io/pypi/v/alifedata-phyloinformatics-convert.svg
        :target: https://pypi.python.org/pypi/alifedata-phyloinformatics-convert

.. image:: https://img.shields.io/travis/mmore500/alifedata-phyloinformatics-convert.svg
        :target: https://travis-ci.com/mmore500/alifedata-phyloinformatics-convert

.. image:: https://readthedocs.org/projects/alifedata-phyloinformatics-convert/badge/?version=latest
        :target: https://alifedata-phyloinformatics-convert.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://zenodo.org/badge/466241441.svg
  :target: https://zenodo.org/doi/10.5281/zenodo.10701178


alifedata-phyloinformatics-convert helps apply traditional phyloinformatics software to alife standardized data


* Free software: MIT license
* Documentation: https://alifedata-phyloinformatics-convert.readthedocs.io.


Built using the :code:`dendropy` library.

Use it as a command line tool to convert to alife standard phylogenetics data

.. code-block::

  Usage: alifedata-phyloinformatics-convert toalifedata [OPTIONS]

    convert standard alife phylogeny data to phloinformatics format

  Options:
    --input-file FILENAME   phyloinformatics data file path; default stdin
    --input-schema TEXT     phyloinformatics data format schema; options include
                            newick, nexml, and nexus  [required]
    --output-file FILENAME  alife data file path; default stdout
    --output-format TEXT    alife data file format; default csv
    --help                  Show this message and exit.


Use it as a command line tool to convert from alife standard phylogenetics data

.. code-block::

  Usage: alifedata-phyloinformatics-convert fromalifedata [OPTIONS]

    convert phloinformatics data to standard alife phylogeny format

  Options:
    --input-file FILENAME   alife data file path; default stdin
    --input-format TEXT     alife data file format; default csv
    --output-file FILENAME  phyloinformatics data file path; default stdout
    --output-schema TEXT    phyloinformatics data format schema; options include
                            newick, nexml, and nexus  [required]
    --help                  Show this message and exit.


Use it as a Python module

.. code-block:: python3

  import alifedata_phyloinformatics_convert as apc

  alife_df = pd.read_csv('alifedata.csv')


  # get a dendropy Tree from alife-standardized phylogeny pandas dataframe
  dendropy_tree = apc.alife_dataframe_to_dendropy_tree(alife_df)

  # get a alife-standardized phylogeny pandas dataframe from a dendropy Tree
  reconverted_alife_df = apc.dendropy_tree_to_alife_dataframe(dendropy_tree)


  # get a biopython Tree from alife-standardized phylogeny pandas dataframe
  biopython_tree = apc.alife_dataframe_to_biopython_tree(alife_df)

  # get a alife-standardized phylogeny pandas dataframe from a biopython Tree
  reconverted_alife_df = apc.dendropy_tree_to_alife_dataframe(biopython_tree)

  # get a networkx DiGraph from alife-standardized phylogeny pandas dataframe
  networkx_digraph = apc.alife_dataframe_to_networkx_digraph(alife_df)

  # get adjacency lists from alife-standardized phylogeny pandas dataframe
  adjjacency_lists = apc.alife_dataframe_to_dict_of_lists(alife_df)

Install from PyPi

.. code-block:: bash

  pip3 install alifedata-phyloinformatics-convert

Citing
------

If alifedata-phyloinformatics-convert is used in scientific publication, please cite it as

    Matthew Andres Moreno and Santiago Rodriguez Papa. (2024). mmore500/alifedata-phyloinformatics-convert. Zenodo. https://doi.org/10.5281/zenodo.10701178

.. code:: bibtex

    @software{moreno2024apc,
      author = {Matthew Andres Moreno AND Santiago Rodriguez Papa},
      title = {mmore500/alifedata-phyloinformatics-convert},
      month = feb,
      year = 2024,
      publisher = {Zenodo},
      doi = {10.5281/zenodo.10701178},
      url = {https://doi.org/10.5281/zenodo.10701178}
    }

And don't forget to leave a `star on GitHub <https://github.com/mmore500/alifedata-phyloinformatics-convert/stargazers>`__!

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
