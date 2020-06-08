import os
import pdfrw





ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
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

data_dict = {
   'introduction': 'The team would like to make an announcement of your death',
   'name': 'Grim Reaper',
   'description': 'Unfortunately by death by having too much fun, you die at 0 year 0 months 1 day from today or at YY/MM/DD'
}

INVOICE_TEMPLATE_PATH = '../docs/death_certificate_template.pdf'
INVOICE_OUTPUT_PATH = "../docs/death_certificate_{fname}.pdf".format(fname = data_dict['name'])

if __name__ == '__main__':
    write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)