import rpa as r
r.init()
r.url('https://www.sec.gov/cgi-bin/browse-edgar?CIK=FIT&owner=exclude&action=getcompany')
r.type('//*[@name="type"]', 'DEFM14A[enter]')
r.click("a#documentsbutton")
# r.download('https://www.sec.gov/Archives/edgar/data/1447599/000162828019015006/fitbitdefinitiveproxy.htm', 'results.html')
r.dump(r.text(), 'results.txt')
