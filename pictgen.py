from argparse import ArgumentParser
import os
import sys
import numpy as np
import csv

# pictgen -p <pict generated file> -t <template file to be modified> -d <delimiter optional> -i <display progress information optional> -e <extension optional>
def parse_options():
    parser = ArgumentParser(description='generate test pattern.')
    parser.add_argument('-p', dest="pict_file", type=str, help='pict generated file', required=True)
    parser.add_argument('-t', dest="template_file", type=str, help='template file to be modified', required=True)
    parser.add_argument('-o', dest="output_file", type=str, help='output file name to be generated')
    parser.add_argument('-d', dest="delimiter", type=str, help='delimiter of pict file. default : \\t')
    parser.add_argument('-i', dest="display_info", action="store_true", help='display progress information')
    parser.add_argument('-e', dest="extension", type=str, help='output\'s extension. default : same as template file')
    return parser.parse_args()


def check_file(file):
    if os.path.isfile(file) == False :
        print (file + " is not found")
        print ("error")
        sys.exit()

def get_filename_info(path):
    name, extension = os.path.splitext(path)
    basename = os.path.basename(name)
    return basename, extension
    
if __name__ == '__main__':
        args = parse_options()
        # print (args.pict_file)
        # print (args.template_file)
        # print (args.delimiter)
        # print (args.display_info)
        # print (args.extension)

        pict_file      = args.pict_file
        template_file  = args.template_file
        output_file    = args.output_file
        delimiter_user = args.delimiter
        display_info   = args.display_info
        extension      = args.extension

        template_basename, template_extension = get_filename_info(template_file)
        
        if extension == None :
            extension = template_extension
        else :
            extension = "." + extension

        if output_file == None :
            output_file = template_basename

        if delimiter_user == None :
            delimiter_user = "\t"

        # check file
        check_file(pict_file)
        check_file(template_file)

        # load pict file
        pict_table = np.genfromtxt(pict_file, delimiter=delimiter_user, dtype=str)

        # load template file
        with open(file=template_file, mode='r') as f:
            template_origin = f.read()

        csv_header = [0]
        csv_header.extend(pict_table[0,:].tolist())

        csv_content = []
        csv_content.append(csv_header)

        digit_len=len(str(len(pict_table)))
        format_str = "{:0" + str(digit_len) + "}"

        for i, pict_row in enumerate(pict_table[1:], start=1) :
            output_file_name = output_file + "_" + format_str.format(i) + extension
            template_modified = template_origin

            csv_row = [i]
            csv_row.extend(pict_row)
            csv_content.append(csv_row)

            with open(file=output_file_name, mode='w') as f:
                for col, pict_element in enumerate(pict_row) :
                    old_str = "${" + pict_table[0,col] + "}"
                    template_modified = template_modified.replace(old_str,pict_element)
                f.write(template_modified)

        with open(output_file + ".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(csv_content)
                

