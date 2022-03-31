import docmaker as dcm

def main():

    document = dcm.Document()
    titles = []
    spam = 3
    date = dcm.date_string()
    conswitch = False

#####____MAKE_SECTION_1__##############

    #Section_Heading_###
    p = document.add_paragraph('')
    runner = p.add_run('Regional Coverage from Pakistan and Kashmir: \n')
    runner.italic= True
    runner.underline= True

    #Section_Body_###
    document, titles = dcm.make_section(document,'',date,spam,titles,True)
    document, titles = dcm.make_section(document,'',date,spam,titles,True)

#####____SAVE_DOCUMENT__###############

    document.save('demo.docx')
    with open('listfile.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % title for title in titles)

if __name__ == '__main__':
    main()
