import sys
from pyfasta import Fasta

key_map = {
"13":"13 dna:chromosome chromosome:GRCh37:13:1:115169878:1 REF",
"GL000226.1":"GL000226.1 dna:supercontig supercontig:GRCh37:GL000226.1:1:15008:1 REF",
"GL000224.1":"GL000224.1 dna:supercontig supercontig:GRCh37:GL000224.1:1:179693:1 REF",
"16":"16 dna:chromosome chromosome:GRCh37:16:1:90354753:1 REF",
"21":"21 dna:chromosome chromosome:GRCh37:21:1:48129895:1 REF",
"10":"10 dna:chromosome chromosome:GRCh37:10:1:135534747:1 REF",
"GL000207.1":"GL000207.1 dna:supercontig supercontig:GRCh37:GL000207.1:1:4262:1 REF",
"GL000209.1":"GL000209.1 dna:supercontig supercontig:GRCh37:GL000209.1:1:159169:1 REF",
"22":"22 dna:chromosome chromosome:GRCh37:22:1:51304566:1 REF",
"GL000241.1":"GL000241.1 dna:supercontig supercontig:GRCh37:GL000241.1:1:42152:1 REF",
"12":"12 dna:chromosome chromosome:GRCh37:12:1:133851895:1 REF",
"GL000248.1":"GL000248.1 dna:supercontig supercontig:GRCh37:GL000248.1:1:39786:1 REF",
"GL000233.1":"GL000233.1 dna:supercontig supercontig:GRCh37:GL000233.1:1:45941:1 REF",
"9":"9 dna:chromosome chromosome:GRCh37:9:1:141213431:1 REF",
"GL000242.1":"GL000242.1 dna:supercontig supercontig:GRCh37:GL000242.1:1:43523:1 REF",
"GL000202.1":"GL000202.1 dna:supercontig supercontig:GRCh37:GL000202.1:1:40103:1 REF",
"6":"6 dna:chromosome chromosome:GRCh37:6:1:171115067:1 REF",
"GL000245.1":"GL000245.1 dna:supercontig supercontig:GRCh37:GL000245.1:1:36651:1 REF",
"14":"14 dna:chromosome chromosome:GRCh37:14:1:107349540:1 REF",
"11":"11 dna:chromosome chromosome:GRCh37:11:1:135006516:1 REF",
"GL000235.1":"GL000235.1 dna:supercontig supercontig:GRCh37:GL000235.1:1:34474:1 REF",
"GL000211.1":"GL000211.1 dna:supercontig supercontig:GRCh37:GL000211.1:1:166566:1 REF",
"X":"X dna:chromosome chromosome:GRCh37:X:1:155270560:1 REF",
"7":"7 dna:chromosome chromosome:GRCh37:7:1:159138663:1 REF",
"20":"20 dna:chromosome chromosome:GRCh37:20:1:63025520:1 REF",
"GL000193.1":"GL000193.1 dna:supercontig supercontig:GRCh37:GL000193.1:1:189789:1 REF",
"GL000195.1":"GL000195.1 dna:supercontig supercontig:GRCh37:GL000195.1:1:182896:1 REF",
"GL000244.1":"GL000244.1 dna:supercontig supercontig:GRCh37:GL000244.1:1:39929:1 REF",
"GL000204.1":"GL000204.1 dna:supercontig supercontig:GRCh37:GL000204.1:1:81310:1 REF",
"GL000192.1":"GL000192.1 dna:supercontig supercontig:GRCh37:GL000192.1:1:547496:1 REF",
"MT":"MT dna:chromosome chromosome:GRCh37:MT:1:16569:1 REF",
"GL000239.1":"GL000239.1 dna:supercontig supercontig:GRCh37:GL000239.1:1:33824:1 REF",
"GL000222.1":"GL000222.1 dna:supercontig supercontig:GRCh37:GL000222.1:1:186861:1 REF",
"GL000219.1":"GL000219.1 dna:supercontig supercontig:GRCh37:GL000219.1:1:179198:1 REF",
"GL000246.1":"GL000246.1 dna:supercontig supercontig:GRCh37:GL000246.1:1:38154:1 REF",
"8":"8 dna:chromosome chromosome:GRCh37:8:1:146364022:1 REF",
"GL000205.1":"GL000205.1 dna:supercontig supercontig:GRCh37:GL000205.1:1:174588:1 REF",
"17":"17 dna:chromosome chromosome:GRCh37:17:1:81195210:1 REF",
"GL000234.1":"GL000234.1 dna:supercontig supercontig:GRCh37:GL000234.1:1:40531:1 REF",
"GL000225.1":"GL000225.1 dna:supercontig supercontig:GRCh37:GL000225.1:1:211173:1 REF",
"GL000237.1":"GL000237.1 dna:supercontig supercontig:GRCh37:GL000237.1:1:45867:1 REF",
"GL000196.1":"GL000196.1 dna:supercontig supercontig:GRCh37:GL000196.1:1:38914:1 REF",
"GL000199.1":"GL000199.1 dna:supercontig supercontig:GRCh37:GL000199.1:1:169874:1 REF",
"GL000194.1":"GL000194.1 dna:supercontig supercontig:GRCh37:GL000194.1:1:191469:1 REF",
"15":"15 dna:chromosome chromosome:GRCh37:15:1:102531392:1 REF",
"GL000238.1":"GL000238.1 dna:supercontig supercontig:GRCh37:GL000238.1:1:39939:1 REF",
"GL000215.1":"GL000215.1 dna:supercontig supercontig:GRCh37:GL000215.1:1:172545:1 REF",
"4":"4 dna:chromosome chromosome:GRCh37:4:1:191154276:1 REF",
"18":"18 dna:chromosome chromosome:GRCh37:18:1:78077248:1 REF",
"GL000227.1":"GL000227.1 dna:supercontig supercontig:GRCh37:GL000227.1:1:128374:1 REF",
"GL000212.1":"GL000212.1 dna:supercontig supercontig:GRCh37:GL000212.1:1:186858:1 REF",
"GL000198.1":"GL000198.1 dna:supercontig supercontig:GRCh37:GL000198.1:1:90085:1 REF",
"Y":"Y dna:chromosome chromosome:GRCh37:Y:2649521:59034049:1 REF",
"GL000214.1":"GL000214.1 dna:supercontig supercontig:GRCh37:GL000214.1:1:137718:1 REF",
"GL000221.1":"GL000221.1 dna:supercontig supercontig:GRCh37:GL000221.1:1:155397:1 REF",
"5":"5 dna:chromosome chromosome:GRCh37:5:1:180915260:1 REF",
"GL000216.1":"GL000216.1 dna:supercontig supercontig:GRCh37:GL000216.1:1:172294:1 REF",
"GL000240.1":"GL000240.1 dna:supercontig supercontig:GRCh37:GL000240.1:1:41933:1 REF",
"1":"1 dna:chromosome chromosome:GRCh37:1:1:249250621:1 REF",
"GL000213.1":"GL000213.1 dna:supercontig supercontig:GRCh37:GL000213.1:1:164239:1 REF",
"GL000228.1":"GL000228.1 dna:supercontig supercontig:GRCh37:GL000228.1:1:129120:1 REF",
"GL000208.1":"GL000208.1 dna:supercontig supercontig:GRCh37:GL000208.1:1:92689:1 REF",
"GL000230.1":"GL000230.1 dna:supercontig supercontig:GRCh37:GL000230.1:1:43691:1 REF",
"GL000206.1":"GL000206.1 dna:supercontig supercontig:GRCh37:GL000206.1:1:41001:1 REF",
"GL000197.1":"GL000197.1 dna:supercontig supercontig:GRCh37:GL000197.1:1:37175:1 REF",
"GL000210.1":"GL000210.1 dna:supercontig supercontig:GRCh37:GL000210.1:1:27682:1 REF",
"GL000218.1":"GL000218.1 dna:supercontig supercontig:GRCh37:GL000218.1:1:161147:1 REF",
"GL000217.1":"GL000217.1 dna:supercontig supercontig:GRCh37:GL000217.1:1:172149:1 REF",
"GL000203.1":"GL000203.1 dna:supercontig supercontig:GRCh37:GL000203.1:1:37498:1 REF",
"GL000236.1":"GL000236.1 dna:supercontig supercontig:GRCh37:GL000236.1:1:41934:1 REF",
"19":"19 dna:chromosome chromosome:GRCh37:19:1:59128983:1 REF",
"2":"2 dna:chromosome chromosome:GRCh37:2:1:243199373:1 REF",
"3":"3 dna:chromosome chromosome:GRCh37:3:1:198022430:1 REF",
"GL000223.1":"GL000223.1 dna:supercontig supercontig:GRCh37:GL000223.1:1:180455:1 REF",
"GL000191.1":"GL000191.1 dna:supercontig supercontig:GRCh37:GL000191.1:1:106433:1 REF",
"GL000200.1":"GL000200.1 dna:supercontig supercontig:GRCh37:GL000200.1:1:187035:1 REF",
"GL000229.1":"GL000229.1 dna:supercontig supercontig:GRCh37:GL000229.1:1:19913:1 REF",
"GL000232.1":"GL000232.1 dna:supercontig supercontig:GRCh37:GL000232.1:1:40652:1 REF",
"GL000231.1":"GL000231.1 dna:supercontig supercontig:GRCh37:GL000231.1:1:27386:1 REF",
"GL000220.1":"GL000220.1 dna:supercontig supercontig:GRCh37:GL000220.1:1:161802:1 REF",
"GL000247.1":"GL000247.1 dna:supercontig supercontig:GRCh37:GL000247.1:1:36422:1 REF",
"GL000249.1":"GL000249.1 dna:supercontig supercontig:GRCh37:GL000249.1:1:38502:1 REF",
"GL000243.1":"GL000243.1 dna:supercontig supercontig:GRCh37:GL000243.1:1:43341:1 REF",
"GL000201.1":"GL000201.1 dna:supercontig supercontig:GRCh37:GL000201.1:1:36148:1 REF"}

def build(args):

    reference = Fasta('/pipeline/data/b37/VEP/homo_sapiens/75/Homo_sapiens.GRCh37.75.dna.primary_assembly.fa')

    with open(args[1], 'r') as ref_file:
        for line in ref_file:
            if line.startswith('#'):
                continue
            fields = line.split('\t')
            chrom = key_map[fields[1]]
            position = int(fields[2])

            ref_allele = reference[chrom][position]

            sys.stdout.write("{}\n".format("\t".join([fields[1], fields[2], ref_allele])))


if __name__ == '__main__':
    build(sys.argv)


