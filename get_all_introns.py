import gffutils

def create_database(input_file, output_file):

    #create database from annotation file

    fn = gffutils.example_filename(input_file)
    db = gffutils.create_db(fn, dbfn=output_file, force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)


def get_introns(database_file, out_introns_file):

    db = gffutils.FeatureDB(database_file, keep_order=True)
    all_introns = open(out_introns_file, "w")
    
    #Create introns

    introns = db.create_introns()

    count = 0
    for i in introns:
        all_introns.write(i['gene_id'][0] + "\t" + str(i.start) +"\t" + str(i.end) + "\t" +  i.strand + "\t" +  'chr' + i.seqid + "\n")
        count = count + 1
    print(count)
    all_introns.close()


if __name__ == "__main__":
    
    in_file = "Homo_sapiens.GRCh37.75.gtf"
    db_file = "test.db"
    introns_file = "all_introns_ensemble75.txt"

    create_database(in_file, db_file)
    get_introns(db_file, introns_file)




