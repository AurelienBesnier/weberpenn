.. image:: https://travis-ci.org/openalea/weberpenn.svg?branch=master
    :target: https://travis-ci.org/openalea/weberpenn

.. contents::

==========
WeberPenn
==========

An extension of the Weber and Penn model

=============
Documentation
=============

.. todo:: Documentation to complete


=================================================
Installation with Miniconda (Windows, linux, OSX)
=================================================

Miniconda installation
----------------------

Follow official website instruction to install miniconda :

http://conda.pydata.org/miniconda.html


1. Create a conda environment and activate it
.............................................

.. code:: shell

    mamba create --name weberpenn openalea.weberpenn -c conda-forge -c openalea3
    mamba activate weberpenn

(Optional) Install several package managing tools :

.. code:: shell

    mamba install notebook nose sphinx sphinx_rtd_theme pandoc coverage

Authors
-------

* Christophe Pradal
