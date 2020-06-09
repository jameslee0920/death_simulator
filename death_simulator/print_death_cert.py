"""
Author: James Bumsoo Lee
This module is designed for the purpose of:
    1. To generate a pre-death certification pdf
To use the functions of the pandas DataFrame:
    import print_death_cert
Specific examples and further documentations of each functions are
included with the respective functions
Requirements:
    Python (version 3.7.4 was used on creation of this module)
    pdfrw (version 0.4 was used on creation of this module)
"""


import pdfrw


ANNOT_KEY = "/Annots"
ANNOT_FIELD_KEY = "/T"
ANNOT_VAL_KEY = "/V"
ANNOT_RECT_KEY = "/Rect"
SUBTYPE_KEY = "/Subtype"
WIDGET_SUBTYPE_KEY = "/Widget"


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    """
    Output a filled Pre-Death Certificate in pdf form. The function takes
    in 3 different values and fills in the values of the respective spots on
    pdf template.  The document is stored in the given filepath.
    Args:
        input_pdf_path (string): filepath containing the template pdf document
        output_pdf_path (string): desired filepath of saved Pre-Death Certification
        data_dict (dictionary): dictionary with 3 indexes of:
            introduction (string): introductory phrase on death certification
            name (string): name of user
            description (string): description of predicted cause of death and age of user
    Returns:
        A pdf document saved on output_pdf_path
    Example:
        data_dict = {
            "introduction": "The team would like to make an announcement of your death",
            "name": "Grim Reaper",
            "description": "Unfortunately you die tomorrow",
        }

        INVOICE_TEMPLATE_PATH = "../docs/death_certificate_template.pdf"
        INVOICE_OUTPUT_PATH = "../docs/death_certificate_{fname}.pdf".format(
            fname=data_dict["name"]
        )

        write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)
    """
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(AP=data_dict[key], V=data_dict[key])
                    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)
