import endangeredanalysis
import endangeredreport


def main():

    # read and analyze input
    filename = input('filename?\n')
    endangeredanalysis.init(filename)

    # produce reports
    report = input('\nreport?\n').strip().title()
    while report != '':
        # print analysis
        analysis = getanalysis(report)
        endangeredreport.status(report, analysis)

        # next report
        report = input('\nreport?\n').strip().title()


def getanalysis(report):
    if report == 'County':
        analysis = endangeredanalysis.county()
    elif report == 'Category':
        analysis = endangeredanalysis.category()
    elif report == 'Taxonomy Group':
        analysis = endangeredanalysis.group()
    elif report == 'Taxonomy Subgroup':
        analysis = endangeredanalysis.subgroup()
    elif report == 'Common Name':
        analysis = endangeredanalysis.common()
    else:
        analysis = {}
    return analysis


main()
