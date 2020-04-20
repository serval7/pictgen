from argparse import ArgumentParser
import os
import sys
import numpy as np

# pictgen -p <pict generated file> -t <template file to be modified> -d <delimiter optional> -i <display progress information optional> -e <extension optional>
def parse_options():
    parser = ArgumentParser(description='generate test pattern.')
    parser.add_argument('-p', dest="pict_file", type=str, help='pict generated file', required=True)
    parser.add_argument('-t', dest="template_file", type=str, help='template file to be modified', required=True)
    parser.add_argument('-o', dest="output_file", type=str, help='output file name to be generated')
    parser.add_argument('-d', dest="delimiter", type=str, help='pict generated file')
    parser.add_argument('-i', dest="display_info", action="store_true", help='display progress information')
    parser.add_argument('-e', dest="extension", type=str, help='output extension')
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

        pict_file     = args.pict_file
        template_file = args.template_file
        output_file   = args.output_file
        delimiter     = args.delimiter 
        display_info  = args.display_info
        extension     = args.extension

        template_basename, template_extension = get_filename_info(template_file)
        
        if extension == None :
            extension = template_extension
        else :
            extension = "." + extension

        if output_file == None :
            output_file = template_basename

        check_file(pict_file)
        check_file(template_file)
        pict_table = np.genfromtxt(pict_file, delimiter="\t", dtype=str)
        
        digit_len=len(str(len(pict_table)))
        format_str = "{:0" + str(digit_len) + "}"

        print (pict_table)
        for i, pict_row in enumerate(pict_table[1:], start=1) :
            output_file_name = output_file + format_str.format(i) + extension
            print (output_file_name)
            # for pict_element in pict_row :
            #     print (pict_element)
                

