import fitz
from RPA.Tables import Tables
from RPA.PDF import PDF


def get_pdf_widgets():

    table = Tables()
    filename = "documents/Generali-page21.pdf"
    doc = fitz.open(filename)
    page = doc.load_page(0)

    columns_list = ['field_name','field_label','field_value']
    mytable = table.create_table(None, False, columns_list)

    # table.add_table_column(mytable, "field_name")
    # table.add_table_column(mytable,"field_label")
    # table.add_table_column("field_value")
    
    list_values=[]
    for field in page.widgets():
        list_values.append(field.field_name)
        list_values.append(field.field_label)
        list_values.append(field.field_value)
        table.add_table_row(mytable, list_values)
        list_values=[]
        # print("field name : %s **** field label : %s **** field value : %s" %(field.field_name,field.field_label,field.field_value))

    rows, columns = mytable.dimensions
    print(rows,columns) 
    for i in range(1, rows):
        row = mytable.get_row(i)
        print(row["field_name"] + " *** " + row["field_label"] + " *** " + row["field_value"])
        #table.group_by_column


def get_pdf_fields():
    pdf = PDF()
    fields = pdf.get_input_fields("documents/Generali-page21.pdf")
    print(fields)

