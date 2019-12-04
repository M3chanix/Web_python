from django.http import Http404, HttpResponse
import sqlite3

def data(request, year):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()
    conn = sqlite3.connect("web.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Itmo")
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    data_dict = {}

    for i in data:
        data_dict[i[0]]=i[1]
    text = data_dict[year]
    #print(data_dict[year])
    html = "<html><body>%s</body></html>" % (text)
    return HttpResponse(html)
