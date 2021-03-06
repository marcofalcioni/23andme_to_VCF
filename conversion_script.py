# encoding: utf-8
"""
    Author: Anna Lewis
    (C) 2014

"""
import sys
import time
import gzip
import os.path

date = time.strftime("%x")


def get_alt_and_genotype(ref, alleles):
    a = alleles[0]
    if len(alleles) == 1:
        if a.lower() == ref.lower():
            alt = "."
            genotype = 0
        else:
            alt = a
            genotype = 1
    else:
        b = alleles[1]
        if a.lower() == ref.lower() and b.lower() == ref.lower():
            alt = "."
            genotype = "0/0"
        elif a.lower() == ref.lower():
            alt = b
            genotype = "0/1"
        elif b.lower() == ref.lower():
            alt = a
            genotype = "0/1"
        elif a.lower() == b.lower():
            alt = a
            genotype = "1/1"
        else:
            alt = "{0},{1}".format(a, b)
            genotype = "1/2"
    return alt, genotype


def main(argv):
    if len(argv) != 3:
        sys.exit("Usage is 'python conversion_script.py "
                 "path/to/23andme_input_file.txt path/to/vcf_output_file.txt'")

    input_filename, output_filename = sys.argv[1:]
    input_data = open(input_filename, 'r')
    if os.path.isfile(output_filename):
        sys.exit("Won't clobber existing file {0}".format(output_filename))

    output_data = open(output_filename, 'w')

    # Load reference genome information
    ref_path = "23andme_reference_genome.txt.gz"
    ref_dict = {}
    with gzip.open(ref_path, 'r') as ref_file:
        for line in ref_file:
            [ref_chr, ref_pos, ref_base] = line.strip().split()
            ref_dict["{0}.{1}".format(ref_chr, ref_pos)] = ref_base

    # Write VCF header
    header = """##fileformat=VCFv4.1
##fileDate={0}
##source=https://github.com/acflewis/23andme_to_VCF.git
##reference=file://{1}
##FORMAT=<ID=GT,Number=1,Type=String,Description=\"Genotype\">
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tGENOTYPE
""".format(date, ref_path)
    output_data.write(header)

    pass_count = 0
    # Process 23andme data, one line at a time
    for line in input_data.readlines():
        if not line.startswith('#'):
            [rsid, chr, pos, alleles] = line.rstrip().split()
            #skip current line if the call was "--", or an indel
            if (alleles == "--" or alleles == "D" or alleles == "I" or
                        alleles == "DI" or alleles == "DD" or
                        alleles == "ID" or alleles == "II"):
                continue
            # Ensure chromosomes named the same as in reference file
            chr = "chr{0}".format(chr)
            # Get the reference base
            ref = ref_dict.get("{0}.{1}".format(chr, pos), "pass")
            if (ref == "pass"):
                pass_count += 1
                continue
            # Get the genotype
            [alt, genotype] = get_alt_and_genotype(ref, alleles)
            output_data.write('{0}\t{1}\t{2}\t{3}\t{4}\t.'
                              '\t.\t.\tGT\t{5}\n'.format(chr, pos, rsid,
                                                         ref.upper(),
                                                         alt.upper(),
                                                         genotype))
    input_data.close()
    output_data.close()
    print("There were {0} variants that were not"
          " matched in the reference file".format(pass_count))

if __name__ == '__main__':
    main(sys.argv)
