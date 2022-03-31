import docmaker as dcm

def main():

    document = dcm.Document()
    titles = []
    spam = 100
    date = dcm.date_string()
    conswitch = True
    tot_js = 0
    dup_limit = 0
    keyterm ='Pakistan'
    blacklist = ['economictimes.indiatimes.com',
    'thehindu.com',
    'indianexpress.com',
    'timesofindia.com',
    'indiatimes.com',
    'aljazeera.com',
    'bbc.co.uk',
    'theguardian.com',
    'theguardian.comworld',
    'thenextweb.com',
    'voxeu.org',
    'theregister.co.uk',
    'searchenginejournal.com',
    'medium.com',
    'telegraph.co.uk',
    'eater.com',
    'maketscreener.com',
    'mashable.com',
    'cjr.org',
    'independant.co.uk',
    'epsncricinfo.com',
    'moneycontrol.com',
    'rt.com',
    'viewfromthewing.com',
    'Fastcompany.com',
    'Coindesk.com',
    'Patheos.com',
    'Wellnessmama.com',
    'Deadline.com',
    'Gulftoday.ae',
    'Matadornetwork.com',
    'Bookriot.com',
    'Independent',
    'Vulture.com',
    'Thejealouscurator.com',
    'Business Insider',
    'Dailycaller.com',
    'Sputniknews.com',
    'Bleedingcool.com',
    'Reviewed.com']

#####____MAKE_SECTION_1__##############
    #Section_Heading_###
    p = document.add_paragraph('')
    runner = p.add_run('Regional Coverage from Pakistan and Kashmir: \n')
    runner.italic= True
    runner.underline= True

    #Section_Body_###
    document, titles, js = dcm.make_section(document,keyterm,date,spam,titles,conswitch,dup_limit,blacklist)
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
