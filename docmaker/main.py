import docmaker as dcm

def main():

    document = dcm.Document()
    titles = []
    spam = 3
    date = dcm.date_string()
    conswitch = True
    tot_js = 0

#####____MAKE_SECTION_1__##############
    #Section_Heading_###
    p = document.add_paragraph('')
    runner = p.add_run('Regional Coverage from Pakistan and Kashmir: \n')
    runner.italic= True
    runner.underline= True

    #Section_Body_###
    document, titles, js = dcm.make_section(document,'Pakistan',date,spam,titles,True)
    tot_js = tot_js + js['totalResults']
    document, titles, js = dcm.make_section(document,'Kashmir',date,spam,titles,True)
    tot_js = tot_js + js['totalResults']

#####____MAKE_SECTION_2__##############

    #Section_Heading_###
    p = document.add_paragraph('')
    runner = p.add_run('Regional Cverage from Iran Iraq and Afghanistan: \n')
    runner.italic= True
    runner.underline= True

    #Section_Body_###
    document, titles, js = dcm.make_section(document,'Iran',date,spam,titles,conswitch)
    tot_js = tot_js + js['totalResults']
    document, titles, js = dcm.make_section(document,'Iraq',date,spam,titles,conswitch)
    tot_js = tot_js + js['totalResults']
    document, titles, js = dcm.make_section(document,'Afghanistan',date,spam,titles,conswitch)
    tot_js = tot_js + js['totalResults']

#####____MAKE_SECTION_3__##############

    #Section_Heading_###
    p = document.add_paragraph('')
    runner = p.add_run('Regional Coverage from India: \n')
    runner.italic= True
    runner.underline= True

    #Section_Body_###
    document, titles, js = dcm.make_section(document,'India',date,spam,titles,conswitch)
    tot_js = tot_js + js['totalResults']

#####____SAVE_DOCUMENT__###############

    p = document.add_paragraph('')
    p.add_run("Number of articles processed: ")
    p.add_run(str(tot_js))
    document.save('demo.docx')
    with open('listfile.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % title for title in titles)

if __name__ == '__main__':
    main()
