#!/usr/bin/env python

import logging, sys, os, shutil, subprocess, argparse
from pathlib import Path
import pandas as pd
import numpy as np

def create_log(filename, filepath = os.getcwd()):
    """Creates a log file and returns the logger object

    Params
    ------
    filename: String
        Name to give the log file

    filepath: String
        Path to the log file (default is cwd)

    Returns
    ------
    logger: Object
        logger object for use in a script

    """
    if filepath == os.getcwd():
            logname = os.getcwd() + '/' + filename
    else:
        try:
            logname = os.path.abspath(filepath) + '/' + filename
        except:
            print(f"Unable to resolve {filepath}. Creating log in cwd.")
            logname = os.getcwd() + '/' + filename
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = logname, format = LOG_FORMAT, level = logging.DEBUG)
    logger = logging.getLogger()
    return(logger)


def file_exists(filename):
    """Checks for existence of a file

    Params
    ------
    file: String
        Name of the file

    Returns
    ------
    Path to file

    """
    if Path(filename).is_file():
        print(f"{filename} found.")
        return(Path(filename).resolve())
    else:
        print(f"{filename} could not be found.")
        sys.exit()


def make_blast_db(reference, dbtype, makeblastdb):
    """Makes a Blast database from a set of reference amplicons

    Params
    ------
    reference: String
        Path to reference amplicon set

    dbtype: String
        Specify nucleotide or protein database

    Returns
    ------

    """
    # Would like to add db_prefix = 'amr2020' so that it's easy to clean up files
    db_name = os.path.splitext(reference)[0]
    p = subprocess.run([makeblastdb, '-in', reference, '-out', db_name, '-dbtype', dbtype])
    if p.returncode != 0:
        print("makeblastdb could not be executed.  Error encountered.")
        print(p.returncode)
    else:
        print("makeblastdb run successfully.")
        return(db_name)


def make_blast_db(reference, dbtype, makeblastdb):
    """Makes a Blast database from a set of reference amplicons

    Params
    ------
    reference: String
        Path to reference amplicon set

    dbtype: String
        Specify nucleotide or protein database

    Returns
    ------

    """
    db_name = os.path.splitext(reference)[0]
    p = subprocess.run([makeblastdb, '-in', reference, '-out', db_name, '-dbtype', dbtype])
    if p.returncode != 0:
        print("makeblastdb could not be executed.  Error encountered.")
        print(p.returncode)
    else:
        print("makeblastdb run successfully.")
        return(db_name)

def run_blast(db, fasta, outfile, blastn, maxhits = 10):
    """Runs Blast on a fasta against a reference database and saves output

    Params
    ------
    ref: String
        Path to reference blast database

    fasta: String
        Specify query fasta sequence

    outfile: String
        Specify output file name

    Returns
    ------
    blast_out: String
        Name of the file containing the blast results
    """
    blast_out = outfile + '_blast.out'
    if maxhits != 10:
        try:
            maxhits + 1 - 1
        except TypeError:
            print(f"You must supply an integer value for max. number of hits. The default is 10.")
            maxhits = 10
        finally:
            maxhits = maxhits
    print(f"Running blast with {maxhits} maximum hits to generate")
    p = subprocess.run(
                [blastn, '-db', db, '-query', fasta, \
                         '-outfmt', \
                         '6 qseqid sseqid qlen slen evalue qcovs pident mismatch', \
                         '-max_target_seqs', str(maxhits), '-out', blast_out])
    if p.returncode != 0:
        print("blastn could not be executed.  Error encountered.")
        print(p.returncode)
    else:
        print("blastn run successfully.")
        print("format: query ID, subject ID, query length, subj length, e val, query cov/subj, percent identical matches, # mismatches")
        return(blast_out)


def get_data(filepath, sep, colnames = None):
    """Creates a pandas df from a csv or txt file

    Params
    ------
    filepath: String
        Path to csv or txt file to import

    sep: String
        Specify field separator (e.g. '\t')

    colnames: List
        Specify a list of column names (don't specify this option if file has a header)

    Returns
    ------
    blast_out: String
        Name of the file containing the blast results
    """
    if colnames is not None:
        return(pd.read_csv(filepath, sep = sep, names = colnames))
    else:
        return(pd.read_csv(filepath, sep = sep))





